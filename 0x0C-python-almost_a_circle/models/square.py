#!/usr/bin/python3
"""
    Module with class Square that inherits
    from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that defines Square objects"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method to initialize square object attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method that returns value of size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Method that sets the value of size"""
        self.width = value
        self.height = value

       
    def __str__(self):
        """Method that prints square objects in given format"""
        sqr = "[Square]"
        _sid = " ({})".format(self.id)
        _sxy = " {}/{} - ".format(self.x, self.y)
        _size = "{}".format(self.width)

        return sqr + _sid + _sxy + _size
