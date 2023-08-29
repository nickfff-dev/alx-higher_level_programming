#!/usr/bin/python3
"""
This module defines a Square class.
The Square class has a private instance attribute size.
"""


class Square:
    """This class defines a square with a private
    instance attribute size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.__size = size
