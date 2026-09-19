#!/usr/bin/env python3
def pow(a, b):
    result = 1
    b = abs(b)
    for i in range(b):
        result = result * a
    return result
