#!/usr/bin/python3

class Square:
    """Class Square that defines square objects
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method that initializeses square objects
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Method that retrieves size of object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets size of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Method that retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method that sets position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method to compute object area
        """
        return self.__size * self.__size

    def my_print(self):
        """Method to print size of square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
