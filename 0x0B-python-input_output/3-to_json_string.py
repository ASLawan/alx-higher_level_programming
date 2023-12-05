#!/usr/bin/python3
"""
    Module with function that returns JSON
    representation of an object

"""
import json


def to_json_string(my_obj):
    """Converts object to JSON format"""
    return json.dumps(my_obj)
