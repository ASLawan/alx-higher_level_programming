#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Class Square that defines square objects
    """
    def __init__(self, size):
        """Method that initializes size of square object

        Args:
            param1 (int): size of square object
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
        """Method that retrieves size of square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set value of square object size

        Args:
            param1 (int): value to set as size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Method to print square object
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
