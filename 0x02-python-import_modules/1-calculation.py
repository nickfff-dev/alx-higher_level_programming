#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5
if __name__ == "__main__":
    addition = add(a, b)
    print('{0} + {1} = {2}'.format(a, b, addition))
    subtraction = sub(a, b)
    print('{0} - {1} = {2}'.format(a, b, subtraction))
    multiplication = mul(a, b)
    print('{0} * {1} = {2}'.format(a, b, multiplication))
    division = div(a, b)
    print('{0} / {1} = {2}'.format(a, b, division))
