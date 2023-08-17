#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return a_dictionary
    else:
        return {k: a_dictionary[k] * 2 for k in list(a_dictionary)}
