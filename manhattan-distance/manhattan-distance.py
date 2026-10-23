import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    return float(np.sum(np.abs(x - y)))