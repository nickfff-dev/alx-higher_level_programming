#!/usr/bin/python3
""" module for function that writes to a file"""


def write_file(filename="", text=""):
    """
    function that writes to a file

    Args:
        filename(str): file path
        text(str): str to write
    """
    with open(filename, "w", encoding='utf-8') as myfile:
        charcnt = myfile.write(text)
    return charcnt
