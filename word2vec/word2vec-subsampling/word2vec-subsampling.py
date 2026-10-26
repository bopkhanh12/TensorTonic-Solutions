import torch

def subsample_keep_probs(counts: torch.Tensor,
                         t: float = 1e-5) -> torch.Tensor:
    """
    Returns the float64 keep probability for every vocabulary word.
    """
    arr = []
    total = torch.sum(counts)
    for i in range(len(counts)):
        temp = counts[i] / total
        arr.append(min(1, torch.sqrt(t / temp)))
    return torch.tensor(arr, dtype=torch.float64)