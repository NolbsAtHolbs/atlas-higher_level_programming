#!/usr/bin/python3

"""Module for function that returns the list of
    available attributes and methods of an object"""


def lookup(obj):
    """(Method) function that looks up an object and returns the list of
        available attributes and methods of an object"""
    return dir(obj)
