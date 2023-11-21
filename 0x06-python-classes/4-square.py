#!/usr/bin/python3

class Square:
    """Class Square that defines square objects
    """
    def __init__(self, size=0):
        """Method to initialize square objects
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that computes area of square object
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Method to retrieve square object size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets value of square object size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
