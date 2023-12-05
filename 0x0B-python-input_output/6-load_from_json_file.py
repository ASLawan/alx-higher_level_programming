#!/usr/bin/python3
"""
    Module with function that creates
    an object from JSON file

"""
import json


def load_from_json_file(filename):
    """creates object from json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
