#!/usr/bin/python3
"""
Function that checks if an object is exactly an instance of
a class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is exactly an instance of
    a class.

    args:
        obj: The instance to check ancestry.
        a_class: The class to check against.

    Returns:
        True: if obj is instance of a_class.
        False: if obj is not an instance of a_class.

    """
    return type(obj) == a_class
