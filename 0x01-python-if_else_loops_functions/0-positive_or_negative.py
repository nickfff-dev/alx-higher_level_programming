#!/usr/bin/python3
import random
number = random.randint(-10, 10)
while True:
    if number > 0:
        print('{:d} is positive'.format(number))
        break
    elif number < 0:
        print('{: d} is negative'.format((number)))
        break
    else:
        print('{:d} is zero'.format(number))
        break
