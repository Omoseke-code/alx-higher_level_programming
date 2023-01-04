#!/usr/bin/python3
"""Defining a rectangle class"""


class Rectangle:
    """defining a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initalisation
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        Rectangle.number_of_instances += 1
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

    def area(self):
        """Area of rectangle"""

        return self.width * self.height

    def perimeter(self):
        """perimeter of rectanglr"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """Returns string to print"""

        if self.width == 0 or self.height == 0:
            return ""
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += str(self.print_symbol)
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """repr"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """destructor"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
