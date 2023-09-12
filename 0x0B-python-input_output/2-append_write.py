#!/usr/bin/python3
""" module for function that appends to a file"""


def append_write(filename="", text=""):
    """
    function that appends to a file

    Args:
        filename(str): file path
        text(str): str to write
    """
    with open(filename, "a", encoding='utf-8') as myfile:
        charcnt = myfile.write(text)
    return charcnt
