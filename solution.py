import pandas as pd
import numpy as np
from scipy.stats import chi2


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    
    # Шаг 2
    x_mean = x.mean()
    s2 = np.var(x, ddof=1)
    
    # Шаг 3
    w = (n - 1) * s2 / 18**2
    
    # Шаг 4
    chi2_left = chi2.ppf(alpha/2, df=n-1)
    chi2_right = chi2.ppf(1-alpha/2, df=n-1)
    
    # Шаг 5
    sigma_left = np.sqrt((n - 1) * s2 / chi2_right)
    sigma_right = np.sqrt((n - 1) * s2 / chi2_left)
    
    # Шаг 7
    return (sigma_left, sigma_right)
