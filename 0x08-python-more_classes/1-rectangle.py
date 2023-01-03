#!/usr/bin/python3
"""Defining a rectangle class"""


class Rectangle:
    """defining a rectangle"""

    def __init__(self, width=0, height=0):
        """initalisation
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter func for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter func for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter func for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter func for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
