import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    fake = np.mean(fake_scores, dtype = float)
    real = np.mean(real_scores, dtype = float)
    return float(fake - real)
    