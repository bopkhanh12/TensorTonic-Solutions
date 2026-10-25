def ordinal_encoding(values: list, ordering: list) -> list:
    """
    Returns the ordinal index of every input value.
    """
    # Write code here
    dic = dict()
    for i in range(len(ordering)):
        dic[ordering[i]] = i
    arr = []
    for str in values:
        arr.append(dic[str])
    return arr