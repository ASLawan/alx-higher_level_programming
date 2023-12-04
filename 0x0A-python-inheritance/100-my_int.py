#!/usr/bin/python3
"""
    Module with class MyInt that inherits
    from int

"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, value):
        """Method that checks if value is != """
        return int.__ne__(self, value)

    def __ne__(self, value):
        """Method that checks if value is == """
        return int.__eq__(self, value)
