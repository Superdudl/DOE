import sys

sys.path.append(__file__)

import numpy as np
import cv2


def match_template(img1, img2):
    if len(img1.shape) == 3 or len(img2.shape) == 3:
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    else:
        gray1 = img1
        gray2 = img2

    h, w = gray1.shape
    center_y, center_x = h // 2, w // 2
    search_area = min(h, w) // 3
    template = gray1[center_y-search_area:center_y+search_area, center_x-search_area:center_x+search_area]
    search_area = gray2
    result = cv2.matchTemplate(search_area, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    best_x, best_y = max_loc
    new_center_y = best_y + template.shape[0] // 2
    new_center_x = best_x + template.shape[1] // 2

    dx = center_x - new_center_x
    dy = center_y - new_center_y

    M = np.float32([[1, 0, dx],
                    [0, 1, dy]])

    aligned_image = cv2.warpAffine(img2, M, (w, h))
    return aligned_image

def match_histograms(source: np.ndarray, reference: np.ndarray):
    if len(source.shape) > 2:
        channels = source.shape[2]
    else:
        channels = 1
        source = np.expand_dims(source, axis=2)
        reference = np.expand_dims(reference, axis=2)

    new_channels = []
    for channel in range(0, channels):
        src = source[:, :].ravel()
        ref = reference[:, :].ravel()

        src_hist, _ = np.histogram(src, bins=256, range=(0, 256), density=True)
        ref_hist, _ = np.histogram(ref, bins=256, range=(0, 256), density=True)

        src_cdf = np.cumsum(src_hist)
        ref_cdf = np.cumsum(ref_hist)

        lut_table = np.zeros(256, dtype=np.uint8)
        img = None
        for i in range(256):
            diff = np.abs(ref_cdf - src_cdf[i])
            lut_table[i] = np.argmin(diff)
        img = cv2.LUT(source[:, :, channel], lut_table)
        new_channels.append(img)

    img = cv2.merge(new_channels)
    return img


def psnr(img1: np.ndarray, img2: np.ndarray, search_area=10) -> float:

    h, w = img2.shape[0:2]
    # img2 = match_histograms(img2, img1)
    mse = np.mean(np.power(img1.astype(np.float32) - img2.astype(np.float32), 2))
    max = 255.0
    psnr = 20 * np.log10(max / np.sqrt(mse))

    # result = cv2.hconcat([img1, img2])
    # while cv2.waitKey(1) != ord('q'):
    #     cv2.imshow("PSNR", result)
    # cv2.destroyWindow('PSNR')
    return psnr


def ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    # Параметры SSIM
    C1 = (0.01 * 255) ** 2
    C2 = (0.03 * 255) ** 2

    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(img1, -1, window)
    mu2 = cv2.filter2D(img2, -1, window)

    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2

    sigma1_sq = cv2.filter2D(img1 ** 2, -1, window) - mu1_sq
    sigma2_sq = cv2.filter2D(img2 ** 2, -1, window) - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window) - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()
