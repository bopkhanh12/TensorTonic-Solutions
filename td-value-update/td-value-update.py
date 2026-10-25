import numpy as np

def td_value_update(V: list, s: int, r: float, s_next: int, alpha: float, gamma: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as V.
    """
    # Write code here
    V_new = np.array(V, dtype=float)
    temp = r + gamma * V_new[s_next] - V_new[s]
    V_new[s] = V_new[s] + alpha * temp
    return V_new