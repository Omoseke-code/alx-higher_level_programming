#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """prints a square with the character #
    Args:
        size (int): size of square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integersize must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()
