#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args < 2:
        print('{:d} arguments:'.format(args - 1))
    elif args == 2:
        print('{0} argument:\n1: {1}'.format(args - 1, sys.argv[1]))
    elif args > 2:
        print('{0} arguments:'.format(args - 1))
        for i in range(1, args):
            print('{0}: {1}'.format(i, sys.argv[i]))
    else:
        print('{}'.format(args - 1))
