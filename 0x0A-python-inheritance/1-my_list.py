#!/usr/bin/python3
"""print sorted"""


class MyList(list):
    """child class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
