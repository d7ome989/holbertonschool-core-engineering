#!/usr/bin/env python3
"""Module that defines Shape, Circle and Rectangle using duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a given shape.

    Args:
        shape: Any object with area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shape_info(circle)
    shape_info(rectangle)
