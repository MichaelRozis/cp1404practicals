"""
CP1404 Practical
Guitar class with name, year, cost, and vintage support.
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Enable sorting by year (oldest first)."""
        return self.year < other.year

    def get_age(self):
        """Calculate age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage (50+ years)."""
        return self.get_age() >= VINTAGE_AGE