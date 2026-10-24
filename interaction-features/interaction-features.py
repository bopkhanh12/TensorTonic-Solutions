def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    # Write code here
    for i in range(len(X)):
        n = len(X[i])
        for j in range(n):
            for k in range(j+1, n):
                X[i].append(X[i][j] * X[i][k])
    return X
    