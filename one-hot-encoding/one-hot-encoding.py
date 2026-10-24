import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.array(y)
    K = num_classes
    if num_classes is None:
        K = int(np.max(y)) + 1
    arr = np.zeros((len(y), K), dtype=float)
    for i in range(len(y)):
        arr[i][y[i]] = 1.0
    return arr