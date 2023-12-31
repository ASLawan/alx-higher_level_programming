#!/usr/bin/python3
"""
    Module that defines an empty
    class

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
