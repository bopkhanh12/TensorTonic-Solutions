def simple_moving_average(values: list, window_size: int) -> list:
    """
    Returns the mean of every complete sliding window.
    """
    # Write code here
    n = len(values) - window_size + 1
    arr = []
    for i in range(n):
        arr.append(sum(values[i:i+window_size]) / window_size)
    return arr