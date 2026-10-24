import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns the bottleneck residual-block output as a nested list.
    """
    W1 = np.array(W1)
    W2 = np.array(W2)
    W3 = np.array(W3)
    Ws = np.array(Ws)
    out = np.maximum(0, x @ W1)
    out = np.maximum(0, out @ W2)
    out = out @ W3
    if Ws is not None:
        y = np.maximum(0, out + x @ Ws)
    return np.round(y, 4).tolist()