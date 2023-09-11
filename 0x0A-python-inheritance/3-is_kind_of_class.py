#!/usr/bin/python3
"""
Function that checks if obj is an instance of a_class
or an instance of a class that inherited from a_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if obj is an instance of a_class
    or an instance of a class that inherited from a_class.

    args:
        obj: the instance.
        a_class: the class.
    Returns:
        True: if both are true.
        False: if either is not true.

    """
    return isinstance(obj, a_class)
