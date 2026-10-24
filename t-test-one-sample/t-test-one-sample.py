import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    s = float(np.sqrt(1/(n - 1) * np.sum((x - np.mean(x)) ** 2)))
    t = float((np.mean(x) - mu0) / (s/np.sqrt(n)))
    return t