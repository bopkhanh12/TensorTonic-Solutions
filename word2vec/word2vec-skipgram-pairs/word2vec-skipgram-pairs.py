import torch

def skipgram_pairs(token_ids: torch.Tensor, window: int) -> torch.Tensor:
    """
    Returns the ordered center-context pairs as an int64 tensor.
    """
    arr = []
    n = len(token_ids)
    for i in range(n):
        for j in range(i - window, i + window + 1):
            if 0 <= j < n and i != j:
                arr.append([token_ids[i], token_ids[j]])
    if not arr:
        return torch.empty((0, 2), dtype=torch.int64)
    return torch.tensor(arr, dtype=torch.int64)