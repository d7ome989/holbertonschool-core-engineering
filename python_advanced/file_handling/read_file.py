#!/usr/bin/env python3
"""Module that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content."""
    with open(filename, "r", encoding="utf-8") as f:
        con = f.read()
        print(con, end="")
