import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    arr = []
    for i in range(k + 1):
        arr.append(math.comb(n,i) * p ** i * (1.0 - p) ** (n - i))
    return {"pmf": float(arr[k]), "cdf": float(sum(arr))}