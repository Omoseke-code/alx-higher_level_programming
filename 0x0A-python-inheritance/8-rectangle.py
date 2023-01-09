#!/usr/bin/python3
"""8-rectangle module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
