#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
This module defines a class Square
with attributes size and methods area

"""


class Square(Rectangle):
    """
    slass Square with attributes size and methods area

    Attributes:
            size(int): the size of the square
    """

    def __init__(self, size):
        """
        initializes a Square instance
        """
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """
        funtion for area

        Returns:
            int: area
        """
        return super().area()
