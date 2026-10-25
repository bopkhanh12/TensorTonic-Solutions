import numpy as np

def clip_gradients(g: list, max_norm: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as g.
    """
    # Write code here
    g = np.array(g)
    temp = np.sqrt(np.sum(g ** 2))
    arr = []
    for num in g:
        if temp <= max_norm:
            arr.append(num)
        else:
            arr.append(num * max_norm / temp)
    return np.array(arr)