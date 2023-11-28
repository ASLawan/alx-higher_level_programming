#!/usr/bin/python3
"""
    Module with class Rectangle that defines rectangle
    class Rectangle

"""


class Rectangle:
    """
        Class Rectangle for creating rectangle objects
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Method to retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Method to retrieve width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
