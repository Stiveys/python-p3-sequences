def print_fibonacci(length):
    """
    Returns the Fibonacci sequence up to the specified length.
    :param length: The number of Fibonacci numbers to generate.
    :return: A list containing the Fibonacci sequence.
    """
    if length == 0:
        return []

    # Initialize the Fibonacci sequence
    fibonacci_sequence = [0]

    if length > 1:
        fibonacci_sequence.append(1)

    # Generate the sequence
    for _ in range(2, length):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # Return the sequence
    return fibonacci_sequence