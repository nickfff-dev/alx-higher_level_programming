#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        print("{}")
    else:
        new_lis = sorted(a_dictionary)
        ([print('{}: {}'.format(item, a_dictionary[item]))
          for item in new_lis])
