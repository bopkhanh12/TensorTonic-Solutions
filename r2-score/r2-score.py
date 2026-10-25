import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    mean = np.mean(y_true)
    if (np.sum((y_true - y_pred) ** 2)) == 0 and (np.sum((y_true - mean) ** 2)) == 0:
        return 1.0
    elif (np.sum((y_true - y_pred) ** 2)) != 0 and (np.sum((y_true - mean) ** 2)) == 0:
        return 0.0
    return float(1 - (np.sum((y_true - y_pred) ** 2)) / (np.sum((y_true - mean) ** 2)))