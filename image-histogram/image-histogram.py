def image_histogram(image: list) -> list:
    """
    Returns a list of intensity and count pairs.
    """
    # Write code here
    dic = dict()
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] in dic:
                dic[image[i][j]] += 1
            else:
                dic[image[i][j]] = 1
    dic = dict(sorted(dic.items(), key=lambda item: item[0]))
    arr = []
    for num in dic:
        arr.append([num, dic[num]])
    return arr