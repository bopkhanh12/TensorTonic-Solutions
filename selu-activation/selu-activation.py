import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    lam = 1.0507
    alpha = 1.6733
    arr = []
    for num in x:
        if num > 0:
            arr.append(lam * num)
        else:
            arr.append(lam * alpha * (math.exp(num) - 1))
    return arr