import sys
sys.path.append(__file__)

import numpy as np

def psnr(bad_img: np.ndarray, good_img: np.ndarray) -> float:
    mse = np.mean(np.power(good_img.astype(np.float32) - bad_img.astype(np.float32), 2))
    if mse == 0:
        return float('inf')
    max = 255.0
    psnr = 20 * np.log10(max/np.sqrt(mse))
    return psnr

