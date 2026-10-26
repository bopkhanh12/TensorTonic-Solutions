import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    arr = [[0.0 for _ in range(size)] for _ in range(size)]
    k = size // 2
    sum_val = 0.0
    for x in range(-k, k + 1):
        for y in range(-k, k + 1):
            val = math.exp(-(x**2 + y**2) / (2 * sigma**2))
            arr[x + k][y + k] = val
            sum_val += val
    for x in range(-k, k + 1):
        for y in range(-k, k + 1):
            arr[x + k][y + k] /= sum_val
    return arr