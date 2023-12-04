#!/usr/bin/python3
"""
    Module class BaseGeometry and class Rectangle
    that inherits from Geometry

"""


class BaseGeometry:
    """An empty class Base Geometry"""

    def area(self):
        """public method that computes area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates given value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from class
        Geometry
    """
    def __init__(self, width, height):
        """Method that initailiazes attributes"""
        self.integer_validator("wdith", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
