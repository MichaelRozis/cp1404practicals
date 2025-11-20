"""
CP1404 Practical - SilverServiceTaxi class
Inherits from Taxi, adds fanciness multiplier and flagfall
Demonstrates proper use of class variable inheritance + DRY principle
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a luxury taxi with fanciness factor and flagfall charge."""
    flagfall = 4.50  # Class variable - same for all silver service taxis

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness  # Override the inherited class variable for this instance

    def __str__(self):
        """Return string representation with flagfall included."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the total fare including flagfall, rounded to nearest 10c."""
        return super().get_fare() + self.flagfall