import numpy as np

def identity_block(x, W1, W2):
    """
    Returns the identity residual-block output as a nested list.
    """
    W1 = np.array(W1)
    W2 = np.array(W2)
    y = np.maximum(0, np.maximum(0, x @ W1.T) @ W2.T + x)
    return y