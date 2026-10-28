def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    # Write code here
    arr = dict()
    for word in values:
        if word in arr:
            arr[word] += 1
        else:
            arr[word] = 1
    array = []
    for word in values:
        array.append(arr[word] / len(values))
    return array