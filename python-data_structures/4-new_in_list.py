#!/usr/bin/python3

def new_in_list(list, index, element):
    if index < 0 or index >= len(list):
        return list.copy()
    else:
        return list[:index] + [element] + list[index+1:]
