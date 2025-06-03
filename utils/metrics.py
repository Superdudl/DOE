import sys

sys.path.append(__file__)

import numpy as np
import cv2


def psnr(img1: np.ndarray, img2: np.ndarray) -> float:
    mse = np.mean(np.power(img1.astype(np.float32) - img2.astype(np.float32), 2))
    if mse == 0:
        return float('inf')
    max = 255.0
    psnr = 20 * np.log10(max / np.sqrt(mse))
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