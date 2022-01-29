import numpy as np

def rmse(predictions,targets):
    """This is root mean square error formula, 
    please use numpy array lists for predictions and targets to get results"""
    return np.sqrt(((predictions-targets)**2).mean())


if __name__ == '__main__':
    d = [0.000, 0.166, 0.333] 
    p = [0.000, 0.254, 0.998]
    print(rmse(np.array(d), np.array(p)))
