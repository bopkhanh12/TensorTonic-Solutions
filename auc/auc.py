import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)
    sum = 0.0
    for i in range(len(fpr) - 1):
        sum += float((fpr[i+1] - fpr[i]) * (tpr[i+1] + tpr[i]) / 2)
    return sum