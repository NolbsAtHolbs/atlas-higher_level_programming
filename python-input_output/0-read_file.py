#!/usr/bin/python3

"""Module for class that reads UTF8 text file and prints it to stdout"""


def read_file(filename=""):
    """function that reads UTF8 text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
