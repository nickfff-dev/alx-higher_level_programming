#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    total = 0
    if args == 1:
        print('{:d}'.format(0))
    else:
        for x in range(1, args):
            total += int(sys.argv[x])
        print('{:d}'.format(total))
