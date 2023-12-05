#!/usr/bin/python3
"""
    Module with class Student that defines
    student

"""


class Student:
    """class Student that defines student objects"""
    def __init__(self, first_name, last_name, age):
        """Method that initializes instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves dictionary
        representation of student instance
        """
        student = self.__dict__.copy()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return student

            new_dict = {}

            for i in range(len(attrs)):
                for s_attr in student:
                    if attrs[i] == s_attr:
                        new_dict[s_attr] = student[s_attr]
            return new_dict
        return student

    def reload_from_json(self, json):
        """Method that replaces all attributes
        of the Student instance"""
        for attr in json:
            self.__dict__[attr] = json[attr]
