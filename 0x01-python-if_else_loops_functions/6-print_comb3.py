#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x + 1, 10):
        if x == 8:
            print("{}{}".format(x, y))
        else:
            print("{}{}".format(x, y), end=", ")
