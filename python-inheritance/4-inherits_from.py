#!/usr/bin/python3

"""Module for function that returns True if object is instance of a class that
inherited (directly or indirectly) from specified class, otherwise False"""


def inherits_from(obj, a_class):
    """Function that checks if object is an inherited instance of a class"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
