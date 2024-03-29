#!/usr/bin/python3

"""This is a module for a function that prints a square with the char #"""


def print_square(size):
    """This function prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for z in range(size):
        print("#" * size)
