#!/usr/bin/python3
"""
    Module with class MyList that inderits
    from list

"""


class MyList(list):
    """Class that defines Mylist"""
    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
