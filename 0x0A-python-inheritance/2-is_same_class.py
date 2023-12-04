#!/usr/bin/python3
"""
Module that checks if an object is an istance of given
class

"""


def is_same_class(obj, a_class):
    """Returns true if obj is instance and
        false otherwise
    """
    return type(obj) is a_class


if __name__ == "__main__":
    is_same_class(obj, a_class)
