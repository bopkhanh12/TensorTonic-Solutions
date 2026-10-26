import numpy as np

def train_discriminator_step(
    real_data: np.ndarray,
    fake_data: np.ndarray,
    D_W: np.ndarray,
    learning_rate: float,
) -> dict:
    """
    Returns updated discriminator weights and the pre-update loss.
    """
    real_data = np.asarray(real_data, dtype=np.float64)
    fake_data = np.asarray(fake_data, dtype=np.float64)
    D_W = np.asarray(D_W, dtype=np.float64)
    n = real_data.shape[0]
    p_real = 1 / (1 + np.exp(-np.dot(real_data, D_W)))
    p_fake = 1 / (1 + np.exp(-np.dot(fake_data, D_W)))
    p_real = np.clip(p_real, 1e-15, 1.0 - 1e-15)
    p_fake = np.clip(p_fake, 1e-15, 1.0 - 1e-15)
    discriminator_loss = float(-(np.sum(np.log(p_real)) + np.sum(np.log(1.0 - p_fake))) / n)
    grad = (np.dot(real_data.T, p_real - 1) + np.dot(fake_data.T, p_fake)) / n
    new_discriminator_weights = D_W - learning_rate * grad
    return {
        "new_discriminator_weights": new_discriminator_weights,
        "discriminator_loss": discriminator_loss
    }