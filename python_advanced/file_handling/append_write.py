#!/usr/bin/env python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 file and return its length."""
    with open(filename, "a", encoding="utf-8") as f:
        app = f.write(text)
        return app
