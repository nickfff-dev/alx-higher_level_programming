#!/usr/bin/python3
""" Represents a Rectangle. """


class Rectangle:
    """ Represents a Rectangle. """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle.
            height(int, optional): Height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of this Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of this Rectangle.

        Args:
            value (int): The new width of the Rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets the height of this Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of this Rectangle.

        Args:
            value (int): The new height of the Rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
