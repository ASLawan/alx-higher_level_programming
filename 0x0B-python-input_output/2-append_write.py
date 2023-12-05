#!/usr/bin/python3
"""
    Module with function that opens text file
    appends to existing text, return characters
    appended
"""


def append_write(filename="", text=""):
    """Function that appends text to files"""
    with open(filename, "a", encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
