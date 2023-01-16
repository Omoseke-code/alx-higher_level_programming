#!/usr/bin/python3
"""base module"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialisation"""
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
