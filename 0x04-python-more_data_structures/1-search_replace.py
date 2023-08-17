#!/usr/bin/python3
def search_replace(my_list, search, replace):
    isEmpty = len(my_list)
    if isEmpty == 0:
        return None
    else:
        new_list = [replace if item == search else item for item in my_list]
        return new_list
