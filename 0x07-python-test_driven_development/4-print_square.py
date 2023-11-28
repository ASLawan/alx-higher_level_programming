#!/usr/bin/python3
"""
    Module with function to print a square
    function receives size and prints it in '#'

"""


def print_square(size):
    """
        Function that prints a square using '#'
    """
    s_msg = "size must be an integer"
    n_msg = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError(s_msg)
    if size < 0:
        raise TypeError(n_msg)
    if isinstance(size, float) and size < 0:
        raise TypeError(s_msg)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
