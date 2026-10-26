def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    # Write code here
    ema = []
    ema.append(values[0])
    for i in range(1, len(values)):
        ema.append(alpha * values[i] + (1 - alpha) * ema[-1])
    return ema