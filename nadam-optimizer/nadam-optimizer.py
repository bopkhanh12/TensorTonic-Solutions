import numpy as np

def nadam_step(w: list, m: list, v: list, grad: list, lr: float = 0.002, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w, new_m, and new_v.
    """
    # Write code here
    w = np.array(w)
    m = np.array(m)
    v = np.array(v)
    grad = np.array(grad)
    m_t = beta1 * m + (1 - beta1) * grad
    v_t = beta2 * v + (1 - beta2) * grad ** 2
    m_t_new = beta1 * m_t + (1 - beta1) * grad
    w_t = w - lr * (m_t_new / (np.sqrt(v_t) + eps))
    return {"new_w": w_t, "new_m": m_t, "new_v": v_t}