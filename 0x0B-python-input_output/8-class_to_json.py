#!/usr/bin/python3
""" function that prints obj dict """


def class_to_json(obj):
    """
    funtion that returns the dictionary description with
    simple data structure

    """
    return obj.__dict__
