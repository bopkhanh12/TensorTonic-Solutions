def warmup_decay_schedule(base_lr: float, warmup_steps: int, total_steps: int, current_step: int) -> float:
    """
    Returns the learning rate for the requested training step.
    """
    # Write code here
    lr = 0
    if current_step < warmup_steps: 
        lr = float(base_lr * current_step / warmup_steps)
    else:
        lr = float(base_lr * (total_steps - current_step) / (total_steps - warmup_steps))
    return lr