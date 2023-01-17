#!/usr/bin/python3
"""models/rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialisation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """display rectangle"""
        d = ""
        if self.height != 0 and self.width != 0:
            d += '\n' * self.y
            for i in range(self.height):
                d += ' ' * self.x
                d += ('#' * self.width)
                if i != self.height - 1:
                    d += '\n'
        print(d)

    def __str__(self):
        """str representation"""
        idd = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(idd, x, y, w, h)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the class"""
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self .x = arg
                elif num == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return {'x': x, 'y': y, 'id': i, 'height': h, 'width': w}
