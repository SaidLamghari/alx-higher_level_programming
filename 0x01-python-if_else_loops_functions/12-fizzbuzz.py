#!/usr/bin/python3

"""Start of the  function that prints
    the numbers from 1 to 100 separated by a space"""


def fizzbuzz():
    for val in range(1, 101):
        if val % 5 == 0 and val % 3 == 0:
            print("FizzBuzz", end=" ")
        elif val % 5 == 0:
            print("Buzz", end=" ")
        elif val % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(val, end=" ")
