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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if value <= 0:
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
        if value <= 0:
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
        if value < 0:
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
        if value < 0:
            raise ValueError("y mmust be >= 0")
        self.__y = value

    def area(self):
        """Computes and returns area of rectangle object"""
        return self.height * self.width

    def display(self):
        """Method that prints object to stdout using '#'"""
        for i in range(self.height):
            if i == 0:
                while self.y > 0:
                    print()
                    self.y -= 1
            for j in range(self.width):
                if j == 0:
                    print(" " * self.x, end='')
                print("#", end='')
            print()

    def __str__(self):
        """Method that prints instance objects in given format"""
        rect = "[Rectangle]"
        _id = " ({})".format(self.id)
        _xy = " {}/{} - ".format(self.x, self.y)
        _wh = "{}/{}".format(self.width, self.height)

        return rect + _id + _xy + _wh

    def update(self, *args, **kwargs):
        """Method that updates object attributes"""
        if args is not None and len(args) != 0:
            attr = ["id", "width", "height", "x", "y"]
            lenn = len(args)
            i = 0
            while i < lenn:
                setattr(self, attr[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Method that returns dictionary representation of Rectangle object"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        rect_dict = {}

        for key in attrs:
            rect_dict[key] = getattr(self, key)

        return rect_dict
