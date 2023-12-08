#!/usr/bin/python3
"""
    Module with class Base


"""
import json


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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns JSON string representation
            of dictionaries
        """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

