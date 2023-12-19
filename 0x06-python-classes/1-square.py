#!/usr/bin/python3
# class Square that defines a square by: (based on 0-square.py)


class Square:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
