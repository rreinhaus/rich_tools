import numpy as np
from rich_tools.math_functions import rmse

def test_rmse():
    d = [0.000, 0.166, 0.333]  
    p = [0.000, 0.254, 0.998]
    assert rmse(np.array(d), np.array(p)) >= 0.38