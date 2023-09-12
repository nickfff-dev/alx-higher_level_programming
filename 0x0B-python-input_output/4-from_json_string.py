#!/usr/bin/python3
""" module for function that prints json rep of obj"""
import json


def from_json_string(my_str):
    """
    function that return  object from json str
    Args:
        my_str: a json string

    Returns:
            JSON: json rep of a string
    """
    return json.loads(my_str)
