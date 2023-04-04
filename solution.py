import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Вычисляем выборочное среднее и стандартное отклонение
    x_mean = np.mean(x)
    x_std = np.std(x, ddof=1)

    # Вычисляем левую и правую границы доверительного интервала
    n = len(x)
    alpha = 1 - p
    z = x_std / np.sqrt(n)
    left = x_mean - z * norm.ppf(1 - alpha / 2)
    right = x_mean - z * norm.ppf(alpha / 2)

    return left, right
