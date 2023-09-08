#!/usr/bin/python3
"""
This function adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    This function adds two integers or floats.

    args:
        a (int, float): The first number to add.
        b (int, float): The second number to add. Default is 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: if a or b is not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
