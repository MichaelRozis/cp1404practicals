"""
CP1404 Practical
Read guitars from file, display, and sort by year.
"""

from prac_07.guitar import Guitar

def main():
    """Load guitars from file, display, and sort by year."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    print("\n... sorted by year (oldest first):")
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars from file and return list of Guitar objects."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars


def display_guitars(guitars):
    """Display each guitar."""
    for guitar in guitars:
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage}")


main()