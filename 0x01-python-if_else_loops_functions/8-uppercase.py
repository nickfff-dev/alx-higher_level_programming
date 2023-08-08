#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            conv = chr(ord(i) - 32)
        else:
            conv = i
        print("{:s}".format(conv), end="")
    print('')
