#!/usr/bin/python3
"""7-base_geometry module"""


class BaseGeometry:
    """has area and integer_validatorvmethod"""
    def area(self):
        """raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(f"<{name}> must be an integer")
        if value <= 0:
            raise ValueError(f"<{name}> must be greater than 0")
