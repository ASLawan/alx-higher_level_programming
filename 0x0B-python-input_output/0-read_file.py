#!/usr/bin/python3
"""
    Module with function that opens reads
    text file and prints it to stdout

"""


def read_file(filename=""):
    """function that opens, reads and prints
        text tile content
    """
    with open(filename, "r", encoding="utf-8") as f:
        fcontent = f.read()
        print(fcontent, end='')
