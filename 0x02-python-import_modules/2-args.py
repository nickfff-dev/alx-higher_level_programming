#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args < 2:
        print('{:d} arguments:'.format(args - 1))
    elif args == 2:
        print('{0} argument:\n1: {1}'.format(args - 1, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(args - 1))
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(sys.argv[1:], start=1)))
