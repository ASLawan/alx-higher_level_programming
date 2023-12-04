#!/usr/bin/python3
"""
    Module with function to check if
    object belong to class or class inherited from
    specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is instance of given
    class
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    is_kind_of_class(obj, a_class)
