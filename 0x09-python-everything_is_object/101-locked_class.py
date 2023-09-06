#!/usr/bin/python3
"""
A class that only allows the creation of the 'first_name' attribute.
Any attempt to create other attributes will raise an AttributeError.
"""


class LockedClass:
    """
    A class that only allows the creation of the 'first_name' attribute.
    Any attempt to create other attributes will raise an AttributeError.
    """
    __slots__ = ['first_name']
