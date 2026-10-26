import torch
import torch.nn.functional as F

def sgns_loss(center_vec: torch.Tensor, pos_vec: torch.Tensor,
              neg_vecs: torch.Tensor) -> torch.Tensor:
    """
    Returns the scalar float64 SGNS loss.
    """
    a = torch.sigmoid(torch.dot(center_vec, pos_vec))
    b = 1.0
    for i in range(len(neg_vecs)):
        b = b * torch.sigmoid(torch.dot(center_vec, -neg_vecs[i]))
    return (- torch.log(a) - torch.log(b))