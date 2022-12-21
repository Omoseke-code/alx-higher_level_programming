#!/usr/bin/python3
"""Defining class"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size**2

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, instance):
        """lesser than comparator"""
        return self.area() < instance.area()

    def __eq__(self, instance):
        """equality comparator"""
        return self.area() == instance.area()

    def __ne__(self, instance):
        """inequality comparator"""
        return self.area() != instance.area()

    def __gt__(self, instance):
        """greater than comparator"""
        return self.area() > instance.area()

    def __ge__(self, instance):
        """greater than or equals to comparator"""
        return self.area() >= instance.area()

    def __le__(self, instance):
        """lesser than or equal comparator"""
        return self.area() <= instance.area()
