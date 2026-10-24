def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    arr = list()
    for i in range(len(points)):
        mini = float('inf')
        idx = 0
        for j in range(len(centroids)):
            dist = sum((points[i][d] - centroids[j][d]) ** 2 for d in range(len(points[i])))
            
            if mini > dist:
                mini = dist
                idx = j
        arr.append(idx)
    return arr