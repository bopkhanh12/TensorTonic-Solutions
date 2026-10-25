import math

def log_transform(values: list) -> list:
    """
    Returns the log1p-transformed values rounded to four decimals.
    """
    # Write code here
    arr = []
    for i in range(len(values)):
        arr.append(math.log(1 + values[i]))
    return arr