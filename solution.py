import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.4
    mu = 300
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)

    t_stat = (x_bar - mu) / (s / np.sqrt(n))
    p_val = 1 - t.cdf(t_stat, n-1)
    
    return True if p_val < alpha else False
