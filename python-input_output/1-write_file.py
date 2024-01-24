#!/usr/bin/python3

"""Module for function that writes a string to a UTF8 text file
and returns the num of chars"""


def write_file(filename="", text=""):
    """function that writes a string to a UTF8 text file
    and returns the num of chars"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
