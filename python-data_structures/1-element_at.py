#!/usr/bin/python3

def element_at(list, index):
    if index < 0 or index >= len(list):
        return None
    else:
        return list[index]
