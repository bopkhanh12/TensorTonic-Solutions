import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.sort(np.array(x))
    q = np.array(q)
    n = x.size
    r = q / 100.0 * (n - 1)
    lower = np.floor(r).astype(int)
    upper = np.ceil(r).astype(int)
    w = r - lower
    return x[lower] * (1 - w) + x[upper] * w