#!/usr/bin/python3
"""
A class that represents a rectangle.
"""


class Rectangle:
    """
    A class that represents a rectangle.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        width (:obj:`int`, optional): The width of the rectangle.
        height (:obj:`int`, optional): The height of the rectangle

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs a new Rectangle with the given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle,
            or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


class RectangleError(Exception):
    """
    Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.
    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
