import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    # Write code here
    arr = []
    for i in range(len(values)):
        theta = 2 * math.pi * values[i] / period
        arr.append([math.sin(theta), math.cos(theta)])
    return arr