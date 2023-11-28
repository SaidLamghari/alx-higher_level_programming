#!/usr/bin/python3



for nbr in range(100):
    if nbr != 99:
        print("{:02d}, ".format(nbr), end="")
    else:
        print("{:02d}".format(nbr))
