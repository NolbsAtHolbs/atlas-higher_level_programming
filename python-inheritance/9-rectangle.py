#!/usr/bin/python3

"""Module for class that inherits from prev files
and adds area, print, and str"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for inherited rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
