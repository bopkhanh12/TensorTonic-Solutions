import torch

def dense_layer_forward(inputs: torch.Tensor, weight_matrix: torch.Tensor, biases: torch.Tensor, nonlinear: bool) -> torch.Tensor:
    """
    Returns an output vector in neuron order, preserving input dtype and device.
    """
    arr = []
    for i in range(len(weight_matrix)):
        a = inputs @ weight_matrix[i] + biases[i]
        if nonlinear == False:
            arr.append(a)
        else:
            arr.append(torch.tanh(a))
    if len(arr) == 0:
        return torch.empty(0, dtype=inputs.dtype, device=inputs.device)
        
    if arr[0].dim() == 0:
        return torch.stack(arr).to(dtype=inputs.dtype, device=inputs.device)
    else:
        return torch.cat(arr, dim=0).to(dtype=inputs.dtype, device=inputs.device)
