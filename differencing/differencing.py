def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    # Write code here
    arr = list(series)
    for _ in range(order):
        num = []
        for i in range(1, len(arr)):
            temp = arr[i] - arr[i - 1]
            num.append(temp)
        arr = num
    return arr