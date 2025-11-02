"""
Estimate: 15 minutes
Actual: 12 minutes
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Storing guitar details."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE