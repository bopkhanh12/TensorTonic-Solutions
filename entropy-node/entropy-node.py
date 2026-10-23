import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    y = np.array(y)
    size = len(y)
    entropy = 0.0
    
    if size == 0: 
        return 0.0
    counts = dict()
    for i in range(len(y)):
        if y[i] in counts:
            counts[y[i]] += 1
        else:
            counts[y[i]] = 1
    
    for count in counts.values():
        p = count / size
        entropy -= p * np.log2(p)
        
    return entropy