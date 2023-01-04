#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """a class with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """This method initialize the object."""
        if hasattr(self, first_name):
            self.first_name = first_name
