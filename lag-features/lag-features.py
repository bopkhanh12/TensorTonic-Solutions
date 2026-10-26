def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    # Write code here
    result = []
    t = max(lags)
    for i in range(t, len(series)):
        arr = []
        for j in range(len(lags)):
                temp = series[i - lags[j]]
                arr.append(temp)
        result.append(arr)
    return result