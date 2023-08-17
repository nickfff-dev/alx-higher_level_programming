#!/usr/bin/python3
def uniq_add(my_list=[]):
    isEmpty = len(my_list)
    if isEmpty == 0:
        return 0
    else:
        result = 0
        for val in set(my_list):
            result += val
        return result
