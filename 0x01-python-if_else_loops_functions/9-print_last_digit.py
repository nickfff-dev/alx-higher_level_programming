#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    trailing_digit = number % 10
    print(trailing_digit, end='')
    return trailing_digit
