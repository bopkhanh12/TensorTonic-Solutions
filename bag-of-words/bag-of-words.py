import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    tokens = np.array(tokens)
    vocab = np.array(vocab)
    dic = dict()
    for word in tokens:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    arr = []
    for word in vocab:
        if word not in dic:
            arr.append(0)
        else:
            arr.append(dic[word])
    return np.array(arr)