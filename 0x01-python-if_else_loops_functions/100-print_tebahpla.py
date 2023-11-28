#!/usr/bin/python3

"""Start of  program that prints the ASCII alphabet,
    in reverse order, alternating lowercase and uppercase
    (z in lowercase and Y in uppercase)"""


for val in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(val) if val % 2 == 0 else chr(val - 32)), end="")
