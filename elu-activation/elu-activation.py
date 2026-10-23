import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    for i in range(len(x)):
        if x[i] > 0:
            continue
        else:
            x[i] = alpha * (math.exp(x[i]) - 1)
    return x