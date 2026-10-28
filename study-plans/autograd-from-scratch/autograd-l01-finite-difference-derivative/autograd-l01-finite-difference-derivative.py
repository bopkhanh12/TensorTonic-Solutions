import numpy as np
def f(coefficients: list, x: float):
    total = 0.0
    for i, c in enumerate(coefficients):
        total += c * (x ** i)
    return float(total)
def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    coefficients = np.array(coefficients)
    val_x = f(coefficients, x)
    val_x_h = f(coefficients, x + h)
    if h == 0:
        slope = 0.0
    else:
        slope = (val_x_h - val_x) / h
        
    return (float(val_x), float(val_x_h), float(slope))