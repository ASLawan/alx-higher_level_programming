#!/usr/bin/python3
"""
    Module with class Rectangle
    that inderits from Base

"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that initialises Rectangle objects"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Method to return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of width"""
        self.__width = value

    @property
    def height(self):
        """Method that returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height value"""
        self.__height = value

    @property
    def x(self):
        """Method that returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method that sets value of x"""
        self.__x = value

    @property
    def y(self):
        """Method that returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method that sets value of y"""
        self.__y = value
