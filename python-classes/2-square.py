#!/usr/bin/python3

"""This is module documentation for a defined Square class"""


class Square:
    """This is a defined Square class documentation"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
