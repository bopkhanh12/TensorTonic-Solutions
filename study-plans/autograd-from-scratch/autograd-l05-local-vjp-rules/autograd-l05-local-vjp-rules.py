def local_vjp(operation: str, inputs: list, output: float, upstream_gradient: float) -> list:
    """
    Returns a list of float gradient contributions in input order.
    """
    arr = []
    
    if operation == "add":
        for i in range(len(inputs)):
            arr.append(float(upstream_gradient))
            
    elif operation == "mul":
        prod = 1.0
        for val in inputs:
            prod *= val
        for i in range(len(inputs)):
            if inputs[i] == 0:
                temp_prod = 1.0
                for j in range(len(inputs)):
                    if j != i:
                        temp_prod *= inputs[j]
                arr.append(float(upstream_gradient * temp_prod))
            else:
                arr.append(float(upstream_gradient * prod / inputs[i]))
    else:
        for i in range(len(inputs)):
            temp = float(upstream_gradient * (1.0 - output**2))
            arr.append(temp)
    return arr