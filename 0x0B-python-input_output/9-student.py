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

    def to_json(self):
        """Public method that retrieves dictionary
        representation of student instance
        """
        return self.__dict__.copy()
