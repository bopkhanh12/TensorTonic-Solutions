import torch
import torch.nn.functional as F

def cbow_forward(context_ids: torch.Tensor, target_id: int,
                 W_in: torch.Tensor, W_out: torch.Tensor) -> torch.Tensor:
    """
    Returns the scalar float64 CBOW cross-entropy loss.
    """
    total = 0.0
    for i in range(len(context_ids)):
        total = total + W_in[context_ids[i]]
    mean = total / len(context_ids)
    z = W_out @ mean
    probs = torch.softmax(z, dim=0)
    return (-torch.log(probs[target_id]))