#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
This module defines a class Square
"""


class Square(Rectangle):
    """
    Class Square with attributes size and methods area

    Attributes:
            size(int): the size of the square
    """
    def __init__(self, size):
        """
        initializes a Square instance
        calls ancestor method integer_validator
        to validate size

        Args:
            size(int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
