#!/usr/bin/python3
"""
module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry.

    Methods:
        area: Raises an Exception.
        integer_validator: Validates that
        a value is a positive integer.
    """

    def area(self):
        """
        Method to calculate the area of the geometry.
        Not yet implemented.
        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate that a value is a positive integer.

        Args:
            name: The name of the value, assumed to be a string.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
