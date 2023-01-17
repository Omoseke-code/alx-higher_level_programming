#!/usr/bin/python3
"""models/square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation"""
        idd = self.id
        x = self.x
        y = self.y
        s = super().width
        return "[Square] ({}) {}/{} - {}".format(idd, x, y, s)

    @property
    def size(self):
        """size getter"""
        return super().width

    @size.setter
    def size(self, size):
        """size setter"""
        super(Square, type(self)).width.fset(self, size)

    def update(self, *args, **kwargs):
        """update"""
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "size" in kwargs:
                self.size = kwargs["size"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        idd = self.id
        x = super().x
        y = super().y
        w = super().width
        return {'x': x, 'y': y, 'id': idd, 'size': w}
