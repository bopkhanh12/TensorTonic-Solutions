import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.array(x)
    pmf = np.where(x == 1, p, 1.0 - p).astype(float)
    e = float(p)
    var = float(p * (1 - p))
    return {"pmf": pmf, "mean": e, "variance": var}