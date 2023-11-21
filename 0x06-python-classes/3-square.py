#!/usr/bin/python3
""" Define class Square."""


class Square:
    """Class Square that defines square objects
    """
    def __init__(self, size=0):
        """Method to initialize object attributes

        Args:
            param1 (int): size of object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method to compute area of square object
        """
        return self.__size * self.__size
