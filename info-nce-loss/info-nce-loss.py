import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    Z1 = np.array(Z1, dtype=np.float64)
    Z2 = np.array(Z2, dtype=np.float64)
    S = (Z1 @ Z2.T) / temperature
    N = len(S)
    
    total_loss = 0.0
    for i in range(N):
        row = S[i]
        max_val = np.max(row)
        log_sum_exp = max_val + np.log(np.sum(np.exp(row - max_val)))
        loss_i = -(row[i] - log_sum_exp)
        total_loss += loss_i
    return float(total_loss / N)