#!/usr/bin/python3

"""Module with rectangle class that creates rectangle
    objects, methods and attributes
"""

class Rectangle:
    """Class that defines rectangle objects"""

    def __init__(self, width=0, height=0):
        """Method to initialize object attributes"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Method that returns object height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets value of object height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Method that returns value of object width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets value of object width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Method that returns area of object"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that returns perimeter of object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Method that prints objects"""
        rectangle = ""

        if self.__height == 0 or self.__width == 0:
            return rectangle

        for i in range(self.__height):
            rectangle += ("#" * self.__width) + "\n"

        return rectangle[:-1]
