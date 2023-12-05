#!/usr/bin/python3
"""
    Module with function that writes an object
    to a textfile using JSON
    representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
