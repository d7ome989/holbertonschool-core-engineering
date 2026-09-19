#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            result += chr(x - 32)
        else:
            result += c
    print(result)
