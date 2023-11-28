#!/usr/bin/python3


for car in range(ord('a'), ord('z')+1):
    if chr(car) not in ['q', 'e']:
        print(chr(car).format(), end="")
