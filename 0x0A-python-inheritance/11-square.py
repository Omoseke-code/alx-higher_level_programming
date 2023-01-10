#!/usr/bin/python3
"""11-square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size**2

    def __str__(self):
        """str"""
        return f"[Square] {self.__size}/{self.__size}"
