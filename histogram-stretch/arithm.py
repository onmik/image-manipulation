import numpy as np

def pow(a, b):
    return np.sign(a) * np.power(np.abs(a), b)

def inval(val):
    return np.where(val <= 0, 1e-4, val)
