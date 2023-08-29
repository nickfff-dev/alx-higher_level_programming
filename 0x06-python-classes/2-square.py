#!/usr/bin/python3
"""
This module defines a Square class.
The Square class has a private instance attribute size.
It also includes type and value checks for the size
attribute during instantiation.
"""


class Square:
    """This class defines a square with a private
    instance attribute size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
