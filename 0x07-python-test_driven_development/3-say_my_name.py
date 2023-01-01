#!/usr/bin/python3
"""Prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints a person's firstname and lastname
    Args:
        first_name (str): firstname
        last_name (str): lastname
    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
