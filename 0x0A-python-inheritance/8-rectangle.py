#!/usr/bin/python3
"""
class Rectangle inherited from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits BaseRectangle

    Attributes:
        width(int): private the width
        height(int): private the height
    """
    def __init__(self, width, height):
        """"
        initialiser for the subclass Rectangle

        Args:
            width(int): should be integer
            height(int): an int
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
