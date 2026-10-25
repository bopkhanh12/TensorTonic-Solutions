import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)
    arr = []
    for i in range(len(x)):
        arr.append(x[i] * (1/(1+np.exp(-x[i]))))
    return np.array(arr)