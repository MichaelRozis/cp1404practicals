"""
CP1404 Practical - Project Management
Estimate: 3 hours
Actual: ALL DAY
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
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "q":
            save_choice = input("Would you like to save to projects.txt? ")
            if save_choice.lower() in ["y", "yes"]:
                save_projects("projects.txt", projects)
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


def filter_projects_by_date(projects):
    """Display projects starting after a given date, sorted by date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%y").date()
    filtered = []
    for project in projects:
        if project.start_date > filter_date:
            filtered.append(project)
    for i in range(len(filtered)):
        for j in range(i + 1, len(filtered)):
            if filtered[i].start_date > filtered[j].start_date:
                temp = filtered[i]
                filtered[i] = filtered[j]
                filtered[j] = temp
    for project in filtered:
        print(str(project))


def save_projects(filename, projects):
    """Save projects to tab-delimited file."""
    out_file = open(filename, 'w')
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
    for project in projects:
        date_str = project.start_date.strftime("%d/%m/%Y")
        line = (project.name + "\t" + date_str + "\t" +
                str(project.priority) + "\t" + str(project.cost) + "\t" +
                str(project.completion) + "\n")
        out_file.write(line)
    out_file.close()


def update_project(projects):
    """Update completion percentage and/or priority of a project."""
    for i in range(len(projects)):
        print(str(i) + " " + str(projects[i]))
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(str(project))
    completion_str = input("New Percentage: ")
    if completion_str != "":
        project.completion = int(completion_str)
    priority_str = input("New Priority: ")
    if priority_str != "":
        project.priority = int(priority_str)


def add_new_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%y").date()
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)


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