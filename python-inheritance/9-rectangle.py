#!/usr/bin/python3

"""Module for class that inherits from prev files
and adds area, print, and str"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for inherited rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def ___str___(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
