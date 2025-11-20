"""
CP1404 Practical
Band class using association
"""

class Band:
    """Represent a band containing a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
