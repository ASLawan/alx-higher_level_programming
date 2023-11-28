#!/usr/bin/python3
"""
Module with function that adds two numbers
the function add_integer(a, b=98) adds two numbers
b has a default value of 98
"""


def add_integer(a, b=98):
    """
        Function that adds two integers and returns sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
