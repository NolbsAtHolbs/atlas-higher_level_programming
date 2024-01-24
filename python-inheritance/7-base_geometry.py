#!/usr/bin/python3

""""Module for class that raises a development exception & validates value"""


class BaseGeometry:
    """Class that raises Exception with message `area() is not implemented`"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
