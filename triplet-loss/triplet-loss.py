import numpy as np
def d(a: float, b: float):
    return (a - b) ** 2
def triplet_loss(anchor: list, positive: list, negative: list, margin: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    anchor = np.array(anchor)
    positive = np.array(positive)
    negative = np.array(negative)
    
    total = 0.0
    
    if anchor.ndim == 1:
        dist_pos = 0.0
        dist_neg = 0.0
        for i in range(len(anchor)):
            dist_pos += d(anchor[i], positive[i])
            dist_neg += d(anchor[i], negative[i])
        
        diff = dist_pos - dist_neg + margin
        total = max(0.0, float(diff))
        return total
        
    else:
        batch_size = len(anchor)
        for i in range(batch_size):
            dist_pos = 0.0
            dist_neg = 0.0
            for j in range(len(anchor[i])):
                dist_pos += d(anchor[i][j], positive[i][j])
                dist_neg += d(anchor[i][j], negative[i][j])
                
            diff = dist_pos - dist_neg + margin
            total += max(0.0, float(diff))
            
        return float(total / batch_size)