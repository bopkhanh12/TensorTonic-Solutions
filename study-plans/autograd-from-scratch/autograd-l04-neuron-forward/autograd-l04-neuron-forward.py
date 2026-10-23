import torch

def neuron_forward(inputs: torch.Tensor, weights: torch.Tensor, bias: torch.Tensor) -> tuple:
    """
    Returns a tuple of scalar tensors: preactivation and tanh output.
    """
    a = np.dot(weights, inputs) + bias
    y = (np.exp(a) - np.exp(-a)) / (np.exp(a) + np.exp(-a))
    return (a, y)