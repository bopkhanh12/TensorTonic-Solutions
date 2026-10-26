import numpy as np

def gan_losses(real_probs: np.ndarray, fake_probs: np.ndarray) -> dict:
    """
    Returns discriminator_loss and generator_loss as Python floats.
    """
    epsilon = 1e-8
    real_probs = np.clip(np.asarray(real_probs, dtype=np.float64), epsilon, 1.0 - epsilon)
    fake_probs = np.clip(np.asarray(fake_probs, dtype=np.float64), epsilon, 1.0 - epsilon)
    real = np.sum(np.log(real_probs))
    fake = np.sum(np.log(1 - fake_probs))
    discriminator_loss = - (real + fake) / len(real_probs)
    generator_loss = - np.sum(np.log(fake_probs)) / len(real_probs)
    return {"discriminator_loss":discriminator_loss,"generator_loss":generator_loss}