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
        to validate type of size

        Args:
            size(int): the size of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method for getting the area of a square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        instance method that prints user friendly format class
        info
        """
        return "[Rectangle] " + \
            str(self.__size) + "/" + str(self.__size)
