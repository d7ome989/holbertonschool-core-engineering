#!/usr/bin/env python3
"""Module that defines a class Square with a private size."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
