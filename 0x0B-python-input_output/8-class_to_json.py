#!/usr/bin/python3
"""8-class_to_json"""


def class_to_json(obj):
    """ retuns the dictionary description with simple data structure """
    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
