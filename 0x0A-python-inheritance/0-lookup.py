#!/usr/bin/python3
"""
Function to return the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Function to return the list of available attributes
    and methods of an object.

    Args:
        obj: The object whose attributes and methods
        are to be listed.

    Returns:
        A list of the attributes and methods of the object.
    """
    return dir(obj)
