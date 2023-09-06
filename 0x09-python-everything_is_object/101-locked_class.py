#!/usr/bin/python3
class LockedClass:
    """
    A class that only allows the creation of the
    'first_name' attribute.
    Any attempt to create other attributes will
    raise an AttributeError.
    """

    def __init__(self):
        """
        Initialize the 'first_name' attribute.
        """
        self.__dict__['first_name'] = None

    def __setattr__(self, name, value):
        """
        Set the value of 'first_name'.
        Raise an AttributeError if any other attribute
        is tried to be set.

        Args:
            name (str): The name of the attribute.
            value: The value to be assigned to the attribute.

        Raises:
            AttributeError: If an attribute other than
            'first_name' is tried to be set.
        """
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' has no attribute {name}")
