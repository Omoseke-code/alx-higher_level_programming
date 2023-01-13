#!/usr/bin/python3
""" 9-student"""


class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary"""
        return self.__dict__.copy()
