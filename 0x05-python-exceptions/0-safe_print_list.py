#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            count += 1
            print(my_list[i], end='')
        except IndexError:
            return count
    print()
    return count
