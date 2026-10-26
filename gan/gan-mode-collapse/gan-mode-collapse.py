import numpy as np

def detect_mode_collapse(generated_samples: np.ndarray, threshold: float = 0.1) -> dict:
    """
    Returns diversity_score and is_collapsed in a dictionary.
    """
    generated_samples = np.asarray(generated_samples, dtype=np.float64)
    n = len(generated_samples)
    if n <= 0:
        return {"diversity_score": 0.0, "is_collapsed": True}
        
    m = len(generated_samples[0])
    total = 0.0
    for j in range(m):
        col = generated_samples[:, j]
        mean = np.mean(col)
        var_j = np.sum((col - mean) ** 2) / n
        s_j = np.sqrt(var_j)
        total += float(s_j)
    diversity_score = float(total / m)
    
    return {
        "diversity_score": diversity_score,
        "is_collapsed": True if diversity_score < threshold else False
    }