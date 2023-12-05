#!/usr/bin/python3
"""
    Module with function that returns the dictionary
    description with a simple data structure
    for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description of an object"""
    new_dict = {}

    if hasattr(obj, "__dict__"):
        new_dict = obj.__dict__.copy()

    return new_dict
