#!/usr/bin/python3
"""
    Module with function that converts JSON
    format data to object (python data structure)

"""
import json


def from_json_string(my_str):
    """function to convert from json to object"""
    return json.loads(my_str)
