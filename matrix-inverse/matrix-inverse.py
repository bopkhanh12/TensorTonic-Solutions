import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.array(A)
    det = np.linalg.det(A)
    if det == 0:
        return None
    return np.linalg.inv(A)