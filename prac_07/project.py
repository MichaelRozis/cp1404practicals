"""
CP1404 Practical
Project class for project management program.
Estimate: 30min
Actual: 25min
"""

import datetime

date_string = input("Date (d/m/yyyy): ")
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))

class Project:
    """Represent a project with name, start date, priority, cost, completion."""

    def __init__(self, name="", start_date=None, priority=0, cost=0.0, completion=0):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string representation of a Project."""
        date_str = self.start_date.strftime("%d/%m/%Y") if self.start_date else "None"
        return (self.name + ", start: " + date_str +
                ", priority " + str(self.priority) +
                ", estimate: $" + str(self.cost) +
                ", completion: " + str(self.completion) + "%")

    def __lt__(self, other):
        """Compare projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion == 100