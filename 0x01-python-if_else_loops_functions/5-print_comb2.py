#!/usr/bin/python3

for nbr in range(100):
    print("{:02d}".format(nbr), end="")
    if nbr != 99:
        print(", ", end="")        
