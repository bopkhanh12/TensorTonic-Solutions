import math

def he_initialization(W: list, fan_in: int) -> list:
    """
    Returns the weights mapped to the He uniform range.
    """
    # Write code here
    l = math.sqrt(6 / fan_in)
    w_new = []
    for i in range(len(W)):
        row = []
        for j in range(len(W[i])):
            row.append(W[i][j] * 2 * l - l)
        w_new.append(row)
    return w_new