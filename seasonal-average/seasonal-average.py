def seasonal_average(series: list, period: int) -> list:
    """
    Returns the average for each position in the seasonal cycle.
    """
    # Write code here
    arr = []
    for i in range(period):
        count = 0
        total = 0.0
        for j in range(i, len(series), period):
            total += series[j]
            count += 1
        if count > 0:
            arr.append(float(total / count))
        else:
            arr.append(0.0)
    return arr