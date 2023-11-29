#!/usr/bin/python3
"""
    Module with class LockedClass
    has not class or object attributes

"""


class LockedClass:
    """class that limits attribute creation
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Init method that does nothing"""
        pass
