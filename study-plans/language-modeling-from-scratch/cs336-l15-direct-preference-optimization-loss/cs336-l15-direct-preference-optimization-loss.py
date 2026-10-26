import torch
import torch.nn.functional as F

def direct_preference_optimization_loss(
    policy_chosen: torch.Tensor, policy_rejected: torch.Tensor,
    reference_chosen: torch.Tensor, reference_rejected: torch.Tensor,
    beta: int | float, label_smoothing: int | float = 0.0,
) -> dict:
    """
    Returns a dict: loss, per_example_loss, chosen_rewards, rejected_rewards, preference_accuracy (tensors).
    """
    n = len(policy_chosen)
    chosen_rewards = []
    rejected_rewards = []
    per_example_loss = []
    
    for i in range(n):
        diff = (policy_chosen[i] - policy_rejected[i]) - (reference_chosen[i] - reference_rejected[i])
        temp = beta * diff
        sig_pos = torch.sigmoid(temp)
        sig_neg = torch.sigmoid(-temp)
        l = -(1.0 - label_smoothing) * torch.log(sig_pos) - label_smoothing * torch.log(sig_neg)
        
        per_example_loss.append(l)
        chosen_rewards.append(beta * (policy_chosen[i] - reference_chosen[i]))
        rejected_rewards.append(beta * (policy_rejected[i] - reference_rejected[i]))
    per_example_loss_tensor = torch.stack(per_example_loss)
    chosen_rewards_tensor = torch.stack(chosen_rewards)
    rejected_rewards_tensor = torch.stack(rejected_rewards)
    
    loss = per_example_loss_tensor.mean()
    preference_accuracy = (chosen_rewards_tensor > rejected_rewards_tensor).to(policy_chosen.dtype).mean()
    
    return {
        "loss": loss,
        "per_example_loss": per_example_loss_tensor,
        "chosen_rewards": chosen_rewards_tensor,
        "rejected_rewards": rejected_rewards_tensor,
        "preference_accuracy": preference_accuracy
    }