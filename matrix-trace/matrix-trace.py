import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A = np.array(A)
    sum = 0.0
    for i in range(len(A)):
        sum += A[i][i]
    return sum