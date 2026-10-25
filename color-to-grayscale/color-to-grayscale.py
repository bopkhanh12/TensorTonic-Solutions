def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    # Write code here
    arr = []
    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            pixel = image[i][j]
            gray_val = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
            row.append(round(gray_val, 3))
        arr.append(row)
    return arr