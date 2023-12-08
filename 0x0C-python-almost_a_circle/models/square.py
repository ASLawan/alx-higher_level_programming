#!/usr/bin/python3
"""
    Module with class Square that inherits
    from Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that defines Square objects"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method to initialize Square object attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method that returns value of size for the object"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Method that sets the value of size for the object"""
        self.width = value
        self.height = value
 
    def __str__(self):
        """Method that prints square objects in given format"""
        sqr = "[Square]"
        _sid = " ({})".format(self.id)
        _sxy = " {}/{} - ".format(self.x, self.y)
        _size = "{}".format(self.width)

        return sqr + _sid + _sxy + _size

    def update(self, *args, **kwargs):
        """Method that updates object attributes"""
        if args != None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            lenn = len(args)
            i = 0
            while i < lenn:
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)
