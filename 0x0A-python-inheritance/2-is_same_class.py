#!/usr/bin/python3
"""2-is_same_clas module"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return type(obj) == a_class
