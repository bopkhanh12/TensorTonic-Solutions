import math

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    dot_product = sum(a * b for a, b in zip(x1, x2))
    norm_x1 = math.sqrt(sum(a ** 2 for a in x1))
    norm_x2 = math.sqrt(sum(b ** 2 for b in x2))
    if norm_x1 == 0 or norm_x2 == 0:
        return 0.0
    cos = dot_product / (norm_x1 * norm_x2)
    if label == 1:
        l = 1 - cos
    else:
        l = max(0, cos - margin)
    return l