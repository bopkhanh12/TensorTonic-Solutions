import numpy as np

def discriminator(x: np.ndarray, W: np.ndarray) -> np.ndarray:
    """
    Returns discriminator probabilities as a float64 array with shape (B, 1).
    """
    temp = x @ W
    arr = []
    for i in range(len(temp)):
        arr.append(1 / (1 + np.exp(-temp[i])))
    return np.array(arr)