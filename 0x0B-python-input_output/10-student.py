#!/usr/bin/python3
""" 9-student"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary"""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
        return self.__dict__
