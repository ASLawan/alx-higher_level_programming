#!/usr/bin/python3
"""
    Module with function that receives
    and prints user's first and last name

"""


def say_my_name(first_name, last_name=""):
    """
        Function that prints user's first and last name
    """
    f_msg = "first_name must be a string"
    l_msg = "last_name must be a string"

    if not first_name or not isinstance(first_name, str):
        raise TypeError(f_msg)
    if not isinstance(last_name, str):
        raise TypeError(l_msg)

    print("My name is {} {}".format(first_name, last_name))
