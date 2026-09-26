#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance with FlyingFish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    ff = FlyingFish()
    ff.fly()
    ff.swim()
    ff.habitat()
    print(FlyingFish.__mro__)
