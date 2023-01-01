#!/usr/bin/python3
"""Indenting"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): text
    Raises:
        TypeError:
        text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = (char + "\n\n").join(
            [sen.strip(" ") for sen in text.split(char)])
    print(text, end="")
