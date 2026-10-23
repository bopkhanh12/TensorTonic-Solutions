import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    x = np.array(X)
    mean_x = np.mean(x, axis = axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)
    std_new = np.where(std > eps, std, 1.0)
    return (x - mean_x) / std_new