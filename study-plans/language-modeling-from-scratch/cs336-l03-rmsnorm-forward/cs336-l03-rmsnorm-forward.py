import torch

def rmsnorm(x: torch.Tensor, g: torch.Tensor, epsilon: float) -> torch.Tensor:
    """
    Returns the RMS-normalized tensor with the same shape and dtype as x.
    """
    return x / (torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + epsilon)) * g
