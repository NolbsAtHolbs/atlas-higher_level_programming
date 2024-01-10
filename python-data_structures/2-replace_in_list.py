#!/usr/bin/python3

def replace_in_list(list, index, element):
    if index >= 0 and index < len(list):
        list[index] = element
    return list
