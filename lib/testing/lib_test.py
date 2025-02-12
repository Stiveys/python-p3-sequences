from lib.sequences import print_fibonacci

def test_print_fibonacci():
    """Tests the print_fibonacci function."""
    assert print_fibonacci(0) == []  # Empty list for length = 0
    assert print_fibonacci(1) == [0]  # Single element for length = 1
    assert print_fibonacci(2) == [0, 1]  # Two elements for length = 2
    assert print_fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21]  # Longer sequence
    assert print_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Full sequence
    