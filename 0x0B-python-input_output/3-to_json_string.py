#!/usr/bin/python3
""" module for function that prints json rep of obj"""
import json


def to_json_string(my_obj):
    """
    function that return json rep of object
    Args:
        my_obj: an object

    Returns:
            str: string rep of obj
    """
    return json.dumps(my_obj)
