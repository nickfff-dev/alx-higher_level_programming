#!/usr/bin/python3
""" module for function that reads a file"""


def read_file(filename=""):
    """ function that reads a file """
    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read())
