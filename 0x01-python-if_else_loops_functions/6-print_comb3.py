#!/usr/bin/python3

for frst in range(10):
    for scd in range(frst + 1, 10):
        if frst != 8 or scd != 9:
            print("{:d}{:d}, ".format(frst, scd), end="")
        else:
            print("{:d}{:d}".format(frst, scd))
