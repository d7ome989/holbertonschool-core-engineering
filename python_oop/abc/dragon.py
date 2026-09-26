#!/usr/bin/env python3
"""Module that demonstrates mixins with a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim and fly."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
