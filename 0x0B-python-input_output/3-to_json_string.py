#!/usr/bin/python3
""" module for function that prints json rep of obj"""
import json


def to_json_string(my_obj):
    """
    return json rep of object
    Args:
        my_obj: an object

    Returns:
            str: string rep of obj
    Raises:
           TypeError: my_obj is not serializable
    """
    try:
        str = json.dumps(my_obj)
        return str
    except TypeError:
        raise TypeError(f'{my_obj} is not JSON serializable')
