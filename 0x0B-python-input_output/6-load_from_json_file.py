#!/usr/bin/python3
"""function that loads json str and parses to obj"""
import json


def load_from_json_file(filename):
    """function that loads json str and parses to obj"""
    with open(filename, 'r', encoding='utf-8') as myfile:
        return json.loads(myfile.read())
