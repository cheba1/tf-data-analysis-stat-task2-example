import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    loc = np.mean(x)
    var = np.var(x)
    # Находим квантили хи-квадрат распределения
    alpha = 1 - p
    chi2_alpha_2 = chi2.ppf(alpha / 2, n - 1)
    chi2_1_alpha_2 = chi2.ppf(1 - alpha / 2, n - 1)
    
    # Вычисляем границы доверительного интервала
    L = (n - 1) * var / chi2_1_alpha_2
    R = (n - 1) * var / chi2_alpha_2
    
    return L, R
