"""
CP1404 Practical
Read, add, sort, and save guitars using Guitar class.
"""

from prac_07.guitar import Guitar


def main():
    """Run the complete guitar program."""
    guitars = load_guitars("guitars.csv")

    print("Guitars from file:")
    display_guitars(guitars)

    add_user_guitars(guitars)
    guitars.sort()

    print("\nAll guitars (sorted by year):")
    display_guitars(guitars)

    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from CSV file into a list."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        line = line.strip()
        if line != "":
            parts = line.split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars


def add_user_guitars(guitars):
    """Add guitars from user input until blank name."""
    print("Add your guitars (blank name to finish):")
    name = input("Name: ").strip()
    while name != "":
        year = get_valid_year()
        cost = get_valid_cost()
        guitars.append(Guitar(name, year, cost))
        print(name + " (" + str(year) + ") : $" + str(cost) + " added.")
        name = input("Name: ").strip()


def get_valid_year():
    """Get positive integer year from user."""
    year = int(input("Year: "))
    while year <= 0:
        print("Year must be > 0")
        year = int(input("Year: "))
    return year


def get_valid_cost():
    """Get positive float cost from user."""
    cost = float(input("Cost: $"))
    while cost <= 0:
        print("Cost must be > 0")
        cost = float(input("Cost: $"))
    return cost


def display_guitars(guitars):
    """Display each guitar with vintage status."""
    for guitar in guitars:
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(str(guitar) + vintage)


def save_guitars(filename, guitars):
    """Save all guitars to CSV file."""
    out_file = open(filename, 'w')
    for guitar in guitars:
        line = guitar.name + "," + str(guitar.year) + "," + str(guitar.cost) + "\n"
        out_file.write(line)
    out_file.close()
    print()
    print(len(guitars), "guitars saved to", filename)


main()