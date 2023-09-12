#!/usr/bin/python3
""" function that writes str rep of object to file"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes str rep of object to file"""
    with open(filename, 'w', encoding='utf-8') as myfile:
        return json.dump(my_obj, myfile)
