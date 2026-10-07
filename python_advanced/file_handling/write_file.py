#!/usr/bin/env python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 file and return its length."""
    with open(filename, "w", encoding="utf-8") as f:
        d = f.write(text)
        return d
