import numpy as np
import cv2

def dwt2d(image):
    """Прямая DWT 2D (Haar)"""
    (h, w) = image.shape
    output = np.zeros_like(image)
    # по строкам
    for i in range(h):
        row = image[i, :]
        output[i, :w//2] = (row[::2] + row[1::2]) / 2
        output[i, w//2:] = (row[::2] - row[1::2]) / 2
    temp = np.copy(output)
    # по столбцам
    for i in range(w):
        col = temp[:, i]
        output[:h//2, i] = (col[::2] + col[1::2]) / 2
        output[h//2:, i] = (col[::2] - col[1::2]) / 2
    return output

def idwt2d(coeffs):
    """Обратная DWT 2D (Haar)"""
    (h, w) = coeffs.shape
    output = np.zeros_like(coeffs)
    temp = np.zeros_like(coeffs)
    # по столбцам
    for i in range(w):
        col_low = coeffs[:h//2, i]
        col_high = coeffs[h//2:, i]
        temp[::2, i] = col_low + col_high
        temp[1::2, i] = col_low - col_high
    # по строкам
    for i in range(h):
        row_low = temp[i, :w//2]
        row_high = temp[i, w//2:]
        output[i, ::2] = row_low + row_high
        output[i, 1::2] = row_low - row_high
    return output

def wavelet_denoise_image(image: np.ndarray, threshold: float = 0.05) -> np.ndarray:
    """
    Простое Wavelet Thresholding для шумоподавления на изображениях ДОЭ.
    Только на numpy и opencv.
    threshold: порог для soft-thresholding (0.02-0.1).
    """

    # Приведение к float [0, 1]
    if image.dtype == np.uint8:
        image_f = image.astype(np.float32) / 255.0
    else:
        image_f = np.clip(image, 0, 1).astype(np.float32)

    # Для цветного изображения - обрабатываем по каналам
    if image_f.ndim == 3 and image_f.shape[2] == 3:
        channels = cv2.split(image_f)
        denoised_channels = []
        for ch in channels:
            coeffs = dwt2d(ch)
            # Применяем soft-thresholding
            coeffs_thr = np.sign(coeffs) * np.maximum(np.abs(coeffs) - threshold, 0)
            ch_denoised = idwt2d(coeffs_thr)
            denoised_channels.append(np.clip(ch_denoised, 0, 1))
        result = cv2.merge(denoised_channels)
    else:
        coeffs = dwt2d(image_f)
        coeffs_thr = np.sign(coeffs) * np.maximum(np.abs(coeffs) - threshold, 0)
        result = idwt2d(coeffs_thr)
        result = np.clip(result, 0, 1)

    return result

def bm3d_like_filter(image: np.ndarray, h: float = 7, bilateral_d: int = 7, bilateral_sigmaColor: int = 15) -> np.ndarray:

    if image.ndim == 3 and image.shape[2] == 3:
        nlm_uint8 = cv2.fastNlMeansDenoisingColored(image, None, h=h, hColor=h, templateWindowSize=7, searchWindowSize=21)
    else:
        nlm_uint8 = cv2.fastNlMeansDenoising(image, None, h=h, templateWindowSize=7, searchWindowSize=21)

    nlm = nlm_uint8.astype(np.float32) / 255.0

    # Gaussian Blur
    smooth = cv2.GaussianBlur(nlm, (bilateral_d | 1, bilateral_d | 1), bilateral_sigmaColor)

    # Blending
    alpha = 0.7
    result = alpha * nlm + (1 - alpha) * smooth
    result = np.clip(result, 0, 1)

    return np.clip(result * 255, 0, 255).astype(np.uint8)