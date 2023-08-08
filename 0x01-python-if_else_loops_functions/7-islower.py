#!/usr/bin/python3

def islower(c):
    if ord(c) < 97:
        return False
    elif ord(c) > 96 and ord(c) < 123:
        return True
