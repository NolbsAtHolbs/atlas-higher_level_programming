#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    max_length = max(len(tuple_a), len(tuple_b))
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]) if max_length > 1 else (tuple_a[0] + tuple_b[0], 0)
