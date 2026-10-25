def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    arr = []
    for word in tokens:
        if word not in stopwords:
            arr.append(word)
    return arr