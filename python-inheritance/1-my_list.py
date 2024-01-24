#!/usr/bin/python3

"""Module for class `MyList` that inherits
a sorted printed list of ints from `list`"""


class MyList(list):
    """Class that will inherit from list"""
    def print_sorted(self):
        print(sorted(self))
