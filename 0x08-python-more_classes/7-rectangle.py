#!/usr/bin/python3
"""
This class provides a Rectangle object.
"""


class Rectangle:
    """
    This class provides a Rectangle object.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): A counter for the
        number of Rectangle instances.
        print_symbol (any type): A symbol for string
        representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the
        rectangle object.

        Parameters:
            width (int): The width of the rectangle.
            Default is 0.
            height (int): The height of the rectangle.
            Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width.

        Parameters:
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
        Getter for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height.

        Parameters:
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
            int: The perimeter of the rectangle.
            If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the print_symbol attribute.

        Returns:
            str: String representation of the rectangle.
            If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + '\n') * self.__height

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate a
        new instance using eval().

        Returns:
            str: String representation of the rectangle in
            the format 'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is
        deleted and decrements the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
