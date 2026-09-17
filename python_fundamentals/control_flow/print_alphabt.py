#!/usr/bin/env python3
import string

result = ""
for letter in string.ascii_lowercase:
    if letter != 'q' and letter != 'e':
        result += letter

print(result)
