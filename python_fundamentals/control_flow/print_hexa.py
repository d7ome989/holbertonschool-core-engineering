#!/usr/bin/env python3
print(*[
    "{} = {}".format(i, hex(i))
    for i in range(99)
], sep="\n")
