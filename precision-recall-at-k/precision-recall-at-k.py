def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    count = 0
    for i in range(k):
        if recommended[i] in relevant:
            count += 1
    precision = count / k
    recall = count / len(relevant)
    return [precision, recall]