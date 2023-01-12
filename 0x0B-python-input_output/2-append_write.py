#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """ a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open(filename,'a', encoding="utf-8") as f:
        return f.write(text)
