#!/usr/bin/python3
"""
    Module with class Base


"""


class Base:
    """Class Base that defines base objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that initialiases object attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
