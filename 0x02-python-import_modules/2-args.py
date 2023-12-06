#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n_as = len(sys.argv) - 1
    if n_as == 0:
        print("0 arguments.")
    elif n_as == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(n_as))
        for i in range(n_as):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
