import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.array(x, dtype=float)
    if x.ndim == 1:
        m = np.max(x)
        exp_x = np.exp(x - m)
        total = np.sum(exp_x)
        arr = exp_x / total
        return arr
    else:
        arr = np.zeros_like(x)
        for i in range(len(x)):
            m = np.max(x[i])
            exp_row = np.exp(x[i] - m)
            total = np.sum(exp_row)
            arr[i] = exp_row / total
        return arr