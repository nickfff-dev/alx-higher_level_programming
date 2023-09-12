#!/usr/bin/python3
"""module for funtion that sets an attribute value"""


def add_attribute(obj, name, value):
    """
    function that sets an attribute value

    Raises:
        TypeError:can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(name, value)
