#!/usr/bin/python3
"""
    Module with class Rectangle that defines
    rectangle objects

"""


class Rectangle:
    """
        Class Rectangle that defines rectangle objects
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method to initialize object attributes"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Method that returns value of object height"""
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
        """Method that sets value of object wdith"""
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
        """Method that prints object in user_friendly output"""
        rectangle = ""

        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += (str(self.print_symbol) * self.__width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Method that prints object in developer_friendly output"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Method that deletes class instance - object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
