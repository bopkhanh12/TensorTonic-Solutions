def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    dic1 = dict()
    dic2 = dict()
    arr = []
    for i in range(len(targets)):
        if categories[i] in dic1:
            dic1[categories[i]] += targets[i]
        else:
            dic1[categories[i]] = targets[i]
    for i in range(len(targets)):
        if categories[i] in dic2:
            dic2[categories[i]] += 1
        else:
            dic2[categories[i]] = 1
    for i in range(len(targets)):
        arr.append(dic1[categories[i]] / dic2[categories[i]])
    return arr