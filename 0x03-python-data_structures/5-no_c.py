#!/usr/bin/python3

def no_c(my_string):
    new_array = list(my_string)
    [new_array.remove(x) for x in new_array if x == 'c' or x == 'C']
    return ''.join(new_array)
