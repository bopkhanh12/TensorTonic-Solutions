import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p = np.array(p)
    y = np.array(y)
    numerator = 2 * np.sum(p * y) + eps
    denominator = np.sum(p) + np.sum(y) + eps
    dice = float(numerator / denominator)
    l = 1 - dice
    return l
