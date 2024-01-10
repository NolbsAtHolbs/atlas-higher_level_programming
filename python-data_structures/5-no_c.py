#!/usr/bin/python3

def print_reversed_list_integer(list=[]):
    for i in range(len(list) - 1, -1, -1):
        print("{:d}".format(list[i]))
