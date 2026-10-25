def moving_median(values: list, window_size: int) -> list:
    """
    Returns the median of every complete sliding window.
    """
    # Write code here
    arr = []
    n = len(values) - window_size + 1
    for i in range(n):
        window = sorted(values[i:i + window_size])
        n = window_size
        if n % 2 == 1:
            arr.append(float(window[n // 2]))
        else:
            arr.append((window[n // 2 - 1] + window[n // 2]) / 2.0)
    return arr