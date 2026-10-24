import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    loss = np.maximum(0, margin - y_true * y_score)
    if reduction == "mean":
        return float(np.mean(loss))
    return float(np.sum(loss))