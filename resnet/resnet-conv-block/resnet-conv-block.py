import numpy as np

def conv_block(x, W1, W2, Ws):
    """
    Returns the projection residual-block output as a nested list.
    """
    W1 = np.array(W1)
    W2 = np.array(W2)
    Ws = np.array(Ws)
    y = np.maximum(0, np.maximum(0, x @ W1) @ W2 + x @ Ws)
    return y