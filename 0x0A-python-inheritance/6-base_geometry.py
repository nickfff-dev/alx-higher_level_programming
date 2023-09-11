#!/usr/bin/python3
"""
module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    class with an area method that raises a not implemented exception

    """
    def area(self):
        """
        that raises an exception.

        Raises:
            Exception: area() is not implemented
        """

        raise Exception("area() is not implemented")
