#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    n_as = len(args)

    if n_as == 0:
        print("0 argument.")
    else:
        print("{} argument{}:".format(n_as, 's' if n_as != 1 else ''))
        for i in range(n_as):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
