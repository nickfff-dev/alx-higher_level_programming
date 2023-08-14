#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg_len = len(sys.argv)
    if arg_len < 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        operator = str(sys.argv[2])
        b = int(sys.argv[3])
        if operator not in ['+', '-', '*', '/']:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
        else:
            if operator == '+':
                result = add(a, b)
                print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
                sys.exit(0)
            elif operator == '-':
                result = sub(a, b)
                print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
                sys.exit(0)
            elif operator == '*':
                result = mul(a, b)
                print('{:d} {!s} {:d} = {:d}'.format(a, operator, b, result))
                sys.exit(0)
            elif operator == '/':
                result = div(a, b)
                print('{:d} {!s} {:d} = {:d}'.format(a, operator, b, result))
                sys.exit(0)
