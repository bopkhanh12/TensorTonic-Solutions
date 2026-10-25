def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    # Write code here
    if min(values) == max(values):
        return [0 for _ in range(len(values))]
    w = (max(values) - min(values)) / num_bins
    arr = []
    for i in range(len(values)):
        arr.append(min(num_bins - 1, int((values[i] - min(values)) / w)))
    return arr