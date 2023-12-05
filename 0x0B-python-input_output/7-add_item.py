#!/usr/bin/python3
"""
    Module with python script that adds all
    arguments to a list and save to a file

"""
import os.path
import sys


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

_list = []
if os.path.exists("add_item.json"):
    _list = load_file("add_item.json")

for arg in sys.argv[1:]:
    _list.append(arg)

save_file(_list, "add_item.json")
