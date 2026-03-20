import numpy as np
import cv2
from time import time

def timeIt(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Частота кадров классического алгоритма: {1/(t2 - t1):.2f} гц')
        return result, (t2 - t1)
    return wrapper

def _smart_edge_aware_filter(image: np.ndarray,
                             gray_blur_ksize: int = 5,
                             canny_t1: int = 50,
                             canny_t2: int = 150,
                             edge_dilate_ksize: int = 3,
                             bilateral_d: int = 9,
                             bilateral_sigma_color: int = 75,
                             bilateral_sigma_space: int = 75,
                             median_ksize: int = 5) -> np.ndarray:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if gray_blur_ksize > 1:
        gray_blur = cv2.GaussianBlur(gray, (gray_blur_ksize, gray_blur_ksize), 0)
    else:
        gray_blur = gray

    edges = cv2.Canny(gray_blur, canny_t1, canny_t2)
    kernel = np.ones((edge_dilate_ksize, edge_dilate_ksize), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)
    bilateral = cv2.bilateralFilter(
        image, d=bilateral_d,
        sigmaColor=bilateral_sigma_color,
        sigmaSpace=bilateral_sigma_space
    )
    median = cv2.medianBlur(image, median_ksize)
    mask_no_edge = (edges_dilated == 0)
    result = np.where(mask_no_edge[..., None], median, bilateral)
    return result.astype(np.uint8)

def _local_wiener_y_channel(bgr: np.ndarray,
                            ksize: int = 5,
                            noise_power = None) -> np.ndarray:

    ycrcb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)

    y_f = y.astype(np.float32) / 255.0

    k = (ksize, ksize)
    mu = cv2.boxFilter(y_f, ddepth=-1, ksize=k, borderType=cv2.BORDER_REFLECT)
    mu2 = cv2.boxFilter(y_f * y_f, ddepth=-1, ksize=k, borderType=cv2.BORDER_REFLECT)
    var = mu2 - mu * mu

    if noise_power is None:
        noise_power = float(np.mean(var))

    eps = 1e-8
    var_safe = var + eps
    gain = 1.0 - noise_power / var_safe
    gain = np.clip(gain, 0.0, 1.0)
    y_wiener = mu + gain * (y_f - mu)
    y_wiener = np.clip(y_wiener, 0.0, 1.0)
    y_out = (y_wiener * 255.0).astype(np.uint8)
    ycrcb_out = cv2.merge((y_out, cr, cb))
    bgr_out = cv2.cvtColor(ycrcb_out, cv2.COLOR_YCrCb2BGR)
    return bgr_out

def _clahe_on_y(bgr: np.ndarray,
                clip_limit: float = 2.0,
                tile_grid_size: tuple[int, int] = (8, 8)) -> np.ndarray:

    ycrcb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    y_clahe = clahe.apply(y)
    ycrcb_out = cv2.merge((y_clahe, cr, cb))
    bgr_out = cv2.cvtColor(ycrcb_out, cv2.COLOR_YCrCb2BGR)
    return bgr_out

def _multiscale_clahe_lab(bgr: np.ndarray,
                          clip_limit_small: float = 2.0,
                          tile_small: tuple[int, int] = (8, 8),
                          clip_limit_large: float = 2.0,
                          tile_large: tuple[int, int] = (16, 16),
                          alpha: float = 0.5) -> np.ndarray:

    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe_small = cv2.createCLAHE(clipLimit=clip_limit_small, tileGridSize=tile_small)
    clahe_large = cv2.createCLAHE(clipLimit=clip_limit_large, tileGridSize=tile_large)

    l_small = clahe_small.apply(l)
    l_large = clahe_large.apply(l)

    l_out = cv2.addWeighted(l_small, alpha, l_large, 1.0 - alpha, 0.0)
    lab_out = cv2.merge((l_out, a, b))
    bgr_out = cv2.cvtColor(lab_out, cv2.COLOR_LAB2BGR)
    return bgr_out

def _adaptive_saturation_hsv(bgr: np.ndarray,
                             s0: float = 0.5,
                             gamma_sat: float = 1.2,
                             gamma_max: float = 1.5,
                             alpha: float = 1.0) -> np.ndarray:

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = cv2.split(hsv)
    s_norm = s / 255.0
    v_norm = v / 255.0
    s0_norm = float(s0)
    mask_low = (s_norm < s0_norm).astype(np.float32)
    gamma_eff = 1.0 + (gamma_max - 1.0) * np.power(1.0 - v_norm, alpha)
    factor = 1.0 + (gamma_sat - 1.0) * mask_low * gamma_eff
    s_new = np.clip(s_norm * factor, 0.0, 1.0)
    s_out = (s_new * 255.0).astype(np.float32)
    hsv_out = cv2.merge((h, s_out, v))
    bgr_out = cv2.cvtColor(hsv_out.astype(np.uint8), cv2.COLOR_HSV2BGR)
    return bgr_out

@timeIt
def restore_doe_image(image: np.ndarray) -> np.ndarray:

    img = image.copy()
    img = _smart_edge_aware_filter(
        img,
        gray_blur_ksize=5,
        canny_t1=50,
        canny_t2=150,
        edge_dilate_ksize=3,
        bilateral_d=9,
        bilateral_sigma_color=75,
        bilateral_sigma_space=75,
        median_ksize=5
    )
    img = _local_wiener_y_channel(img, ksize=5, noise_power=None)
    img = _clahe_on_y(img, clip_limit=2.0, tile_grid_size=(8, 8))
    img = _smart_edge_aware_filter(
        img,
        gray_blur_ksize=3,
        canny_t1=40,
        canny_t2=120,
        edge_dilate_ksize=3,
        bilateral_d=7,
        bilateral_sigma_color=60,
        bilateral_sigma_space=60,
        median_ksize=3
    )

    img = _multiscale_clahe_lab(
        img,
        clip_limit_small=2.0, tile_small=(8, 8),
        clip_limit_large=2.0, tile_large=(16, 16),
        alpha=0.5
    )

    img = _adaptive_saturation_hsv(
        img,
        s0=0.5,
        gamma_sat=1.2,
        gamma_max=1.5,
        alpha=1.0
    )

    img = _smart_edge_aware_filter(
        img,
        gray_blur_ksize=3,
        canny_t1=40,
        canny_t2=120,
        edge_dilate_ksize=3,
        bilateral_d=5,
        bilateral_sigma_color=50,
        bilateral_sigma_space=50,
        median_ksize=3
    )

    return img

if __name__ == "__main__":
    from metrics import psnr, ssim
    original_path = "C:/Projects/Datasets/DOE/custom_data/target_test/20250919_152955_845910.bmp"
    blurred_path = "C:/Projects/Datasets/DOE/custom_data/input_test/20250919_152955_845910.bmp"

    original = cv2.imread(original_path)
    blurred = cv2.imread(blurred_path)

    restored, _ = restore_doe_image(blurred)

    PSNR = psnr(restored, original)
    SSIM = ssim(restored, original)

    print(f"PSNR = {PSNR:.2f}\nSSIM = {SSIM:.2f}")

    cv2.namedWindow("RESULT", cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow("RESULT", cv2.hconcat([original, blurred, restored]))
    cv2.waitKey(0)