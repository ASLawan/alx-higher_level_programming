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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes JSON string representation of
            list_obj to a file
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None:
            list_objs = []
            list_dict.append(list_objs.to_dictionary())
        else:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of JSON string representation"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all atributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(10, 10)
        else:
            new_instance = cls(10)

        new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """method that returns list of instances"""
        file = "{}.json".format(cls.__name__)
        try:
            with open(file, 'r') as f:
                json_string = f.read()
                list_dict = cls.from_json_string(json_string)
                list_instances = [cls.create(**dict) for dict in list_dict]
                return list_instances
        except FileNotFoundError:
            return []
