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
