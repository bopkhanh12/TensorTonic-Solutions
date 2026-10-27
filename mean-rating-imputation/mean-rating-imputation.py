def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    """
    Returns a copy with missing ratings replaced by user or item means.
    """
    # Write code here
    matrix_copy = [row[:] for row in ratings_matrix]
    if mode == "user":
        for i in range(len(matrix_copy)):
            total = 0
            count = 0
            for j in range(len(matrix_copy[i])):
                total += matrix_copy[i][j]
                if matrix_copy[i][j] != 0:
                    count += 1
            if count == 0: 
                continue
            for j in range(len(matrix_copy[i])):
                if matrix_copy[i][j] == 0:
                    matrix_copy[i][j] = float(total / count)
                    
    elif mode == "item":
        for i in range(len(matrix_copy[0])):
            total = 0
            count = 0
            for j in range(len(matrix_copy)):
                total += matrix_copy[j][i]
                if matrix_copy[j][i] != 0:
                    count += 1
            if count == 0: 
                continue
            for j in range(len(matrix_copy)):
                if matrix_copy[j][i] == 0:
                    matrix_copy[j][i] = float(total / count)
    return matrix_copy