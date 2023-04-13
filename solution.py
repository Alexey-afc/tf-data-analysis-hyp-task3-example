import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
import random


chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
   if ztest(x,300)[1] < 0.04:
        return True
    else:
        return False
