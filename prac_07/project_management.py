"""
CP1404 Practical - Project Management
Estimate: 3 hours
Actual:
"""


import datetime

from prac_07.project import Project

def main():
    """Run project management program with menu."""
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print("Loaded " + str(len(projects)) + " projects from projects.txt")

    choice = ""
    while choice != "q":
        print_menu()
        choice = input(">>> ").lower()
        if choice == "d":
            display_projects(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu choice")


def print_menu():
    """Display menu options."""
    print("- (L)oad projects  ")
    print("- (S)ave projects  ")
    print("- (D)isplay projects  ")
    print("- (F)ilter projects by date")
    print("- (A)dd new project  ")
    print("- (U)pdate project")
    print("- (Q)uit")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = []
    completed = []
    for project in projects:
        if project.is_complete():
            completed.append(project)
        else:
            incomplete.append(project)

    incomplete.sort()
    completed.sort()

    print("Incomplete projects: ")
    for project in incomplete:
        print("  " + str(project))

    print("Completed projects: ")
    for project in completed:
        print("  " + str(project))


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        line = line.strip()
        if line != "":
            parts = line.split('\t')
            name = parts[0]
            date_str = parts[1]
            priority = int(parts[2])
            cost = float(parts[3])
            completion = int(parts[4])
            start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            project = Project(name, start_date, priority, cost, completion)
            projects.append(project)
    in_file.close()
    return projects


main()