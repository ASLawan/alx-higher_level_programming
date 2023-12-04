#!/usr/bin/python3
"""
    Module with function to check if given object
    is an instance of class with direct or indirect
    inheritance of given class
"""


def inherits_from(obj, a_class):
    """Returns true if object is instance and
    false otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)


if __name__ == "__main__":
    inherits_from()
