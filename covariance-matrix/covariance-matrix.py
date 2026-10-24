import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x = np.array(X)
    mean = np.mean(x, axis=0)
    x_c = x - mean
    return x_c.T @ x_c / (len(x) - 1)