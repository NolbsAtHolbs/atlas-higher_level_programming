#!/usr/bin/python3

"""Module for class that raises a development exception"""


class BaseGeometry:
    """Class that raises Exception with message `area() is not implemented`"""
    def area(self):
        raise Exception('area() is not implemented')
