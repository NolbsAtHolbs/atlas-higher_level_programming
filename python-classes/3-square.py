#!/usr/bin/python3

"""This is module documentation for a defined area of Square class"""


class Square:
    """This is class documentation for the area of a defined Square"""
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size #comment test
