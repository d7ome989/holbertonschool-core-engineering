#!/usr/bin/env python3
def get_or_zero(t, idx):
    if idx >= len(t):
        return 0
    else:
        return t[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    first = get_or_zero(tuple_a, 0) + get_or_zero(tuple_b, 0)
    second = get_or_zero(tuple_a, 1) + get_or_zero(tuple_b, 1)
    return (first, second)
