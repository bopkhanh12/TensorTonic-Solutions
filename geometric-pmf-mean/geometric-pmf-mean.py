import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    # Write code here
    k = np.array(k)
    pmf = np.zeros(len(k))
    for i in range(len(k)):
        pmf[i] = np.pow((1 - p), (k[i] - 1)) * p
    mean = 1/p
    return {"pmf" : pmf, "mean" : mean}
        