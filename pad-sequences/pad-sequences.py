import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    seqs = [list(seq) for seq in seqs]
    if max_len is not None:
        max_val = max_len
    else:
        max_val = 0
        for i in range(len(seqs)):
            if max_val < len(seqs[i]):
                max_val = len(seqs[i])
    for i in range(len(seqs)):
        if len(seqs[i]) > max_val:
            seqs[i] = seqs[i][:max_val]
        elif len(seqs[i]) < max_val:
            for _ in range(max_val - len(seqs[i])):
                seqs[i].append(pad_value)
    if len(seqs) == 0:
        return np.zeros((0, max_val), dtype=int)
    return np.array(seqs)