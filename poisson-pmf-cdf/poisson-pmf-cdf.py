import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    arr = []
    for i in range(k + 1):
        p = (math.exp(-lam) * (lam ** i)) / math.factorial(i)
        arr.append(p)
    return {"pmf": float(arr[k]), "cdf": float(math.fsum(arr))}