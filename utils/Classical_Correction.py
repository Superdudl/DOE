import cv2
import numpy as np
from scipy.signal import wiener

# ======= Умная медианная фильтрация с сохранением границ =======
def smart_median_filter(image, median_ksize=5, edge_ksize=3, canny_threshold1=50, canny_threshold2=150,
                         bilateral_d=9, bilateral_sigma_color=75, bilateral_sigma_space=75):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)
    kernel = np.ones((edge_ksize, edge_ksize), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)
    bilateral_filtered = cv2.bilateralFilter(image, bilateral_d, bilateral_sigma_color, bilateral_sigma_space)
    median_filtered = cv2.medianBlur(image, median_ksize)
    mask = edges_dilated == 0
    result = np.where(mask[..., None], median_filtered, bilateral_filtered)
    return result.astype(np.uint8)

# ======= Восстановление с помощью фильтра Винера и CLAHE =======
def restore_with_wiener_clahe(image, kernel_size=5, clip_limit=4.0, tile_grid_size=(6, 6)):
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv)
    y_wiener = wiener(y.astype(np.float32), kernel_size)
    y_wiener = np.clip(y_wiener, 0, 255).astype(np.uint8)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    y_clahe = clahe.apply(y_wiener)
    restored_yuv = cv2.merge([y_clahe, u, v])
    return cv2.cvtColor(restored_yuv, cv2.COLOR_YUV2BGR)

# ======= Цветовая коррекция: CLAHE + усиление насыщенности =======
def adaptive_color_correction(image, clip_limit=2.5, tile_grid_size=(8, 8), saturation_boost=1.1):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    l = clahe.apply(l)
    l = cv2.medianBlur(l, 5)
    lab = cv2.merge([l, a, b])
    corrected = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    hsv = cv2.cvtColor(corrected, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = cv2.split(hsv)
    s = np.where(s < 128, s * saturation_boost, s)
    s = np.clip(s, 0, 255)
    hsv = cv2.merge([h, s, v])
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

# ======= Основная функция восстановления изображения =======
def restore_image(image, apply_final_median=True):
    """
    Полная цепочка восстановления изображения, искажённого ДОЭ.
    :param image: BGR изображение
    :param apply_final_median: Применять ли медианный фильтр в конце
    :return: Обработанное изображение
    """
    denoised = smart_median_filter(image)
    restored = restore_with_wiener_clahe(denoised)
    restored = smart_median_filter(restored)
    final_result = adaptive_color_correction(restored)
    if apply_final_median:
        final_result = smart_median_filter(final_result)
    return final_result
