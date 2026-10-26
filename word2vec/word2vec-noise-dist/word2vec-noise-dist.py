import torch

def noise_distribution(counts: torch.Tensor,
                       alpha: float = 0.75) -> torch.Tensor:
    """
    Returns the float64 negative-sampling distribution over the vocabulary.
    """
    total = torch.sum(counts ** alpha)
    arr = []
    for num in counts:
        arr.append((num ** alpha) / total)
    return torch.tensor(arr, dtype = torch.float64)