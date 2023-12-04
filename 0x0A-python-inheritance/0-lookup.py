#!/usr/bin/python3
"""
    Module with function that returns
    list of object's attributes and
    methods
"""


def lookup(obj):
    """
        returns available attributes and methods
    """
    return dir(obj)


if __name__ == "__main__":
    lookup(obj)
