#!/usr/bin/python3
"""
Function that checks if obj is an subclass of a_class
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is an subclass of a_class

    args:
        obj: the subclass.
        a_class: the class.

    Returns:
        True: if obj is subclass of a_class.
        False: if obj is not an subclass of a_class.

    """
    return issubclass(obj, a_class)
