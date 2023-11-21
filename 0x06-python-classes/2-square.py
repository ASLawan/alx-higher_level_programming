#!/usr/bin/python3
"""Define class Square."""


class Square:
    """A class Square that defines a square
    """
    def __init__(self, size=0):
        """
        Method to initliaze object attributes
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
