#!/usr/bin/python3
"""
    Module with function class Rectangle 
    Creates class objects attributes and methods
"""

class Rectangle:
    """
        class that creates rectangle objects
    """
    def __init__(self, width=0, height=0):
        """method that initializes attributes"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Method that returns value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Method that returns value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Method that returns area of triangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
