#!/usr/bin/python3

"""Defining class"""


class Square:
    """A class for a square"""
    def __init__(self, size=0):
        """Initialise a square class.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
