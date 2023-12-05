#!/usr/bin/python3
"""
    Module woth functiont that writes to a
    text file
    creates file or overwrites it
"""


def write_file(filename="", text=""):
    """Function that writes to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
