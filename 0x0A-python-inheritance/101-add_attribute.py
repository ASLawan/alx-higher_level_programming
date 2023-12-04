#!/usr/bin/python3
"""
    Module with function that adds attribute
    to an object if possible

"""


def add_attribute(obj, name, value):
    """Method that adds attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
