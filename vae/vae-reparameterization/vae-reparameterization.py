import numpy as np

def reparameterize(mu: np.ndarray, log_var: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """
    Returns the float64 latent sample with the same shape as mu.
    """
    var = np.exp(1 / 2 * log_var)
    z = mu + var * epsilon
    return z