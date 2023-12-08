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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width mmust be > 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method that returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method that sets value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x mmust be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method that returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method that sets value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y mmust be >= 0")
        self.__y = value

    
    def area(self):
        """Computes and returns area of rectangle object"""
        return self.__height * self.__width

    def display(self):
        """Method that prints object to stdout using '#'"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Method that prints instance objects in given format"""
        rect = "[Rectangle]"
        _id = " ({})".format(self.id)
        _xy = " {}/{} - ".format(self.__x, self.__y)
        _wh = "{}/{}".format(self.__width, self.__height)

        return rect + _id + _xy + _wh

