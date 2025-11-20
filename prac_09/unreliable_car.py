"""
CP1404 Practical - UnreliableCar class that inherits from Car.
Demonstrates overriding with random behaviour - required by the practical.
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent a car with a chance of not driving (unreliable)."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return string representation including reliability."""
        return f"{super().__str__()}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive only if random number (0-100) is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
