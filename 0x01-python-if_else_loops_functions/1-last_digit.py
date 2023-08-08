#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while True:
    if number % 10 == 0:
        print('Last digit of {:d} is {:d} and is 0'
              .format(number, number % 10))
        break
    elif number < 0:
        print('Last digit of {:d} is -{:d} and is less than 6 and not 0'
              .format(number, abs(number) % 10))
        break
    else:
        if number % 10 > 5:
            print('Last digit of {:d} is {:d} and is greater than 5'
                  .format(number, number % 10))
            break
        else:
            print('Last digit of {:d} is {:d} and is less than 6 and not 0'
                  .format(number, number % 10))
            break
