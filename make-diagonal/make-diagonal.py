import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    v = np.array(v)
    arr = np.zeros((v.size, v.size), dtype=v.dtype)
    for i in range(len(arr)):
        arr[i][i] = v[i]
    return arr