import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    s_2 = float(np.var(x, ddof=1))
    s = float(np.sqrt(s_2))
    return {"variance":s_2, "standard_deviation": s}