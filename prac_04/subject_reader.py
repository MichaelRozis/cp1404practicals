"""Read and process subject data from a text file into a structured format."""

FILENAME = "subject_data.txt"


def main():
    """Load and display subject details from file."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read subject data from file and return as list of lists."""
    subject = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert student number to integer
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display details for each subject including code, lecturer, and student count."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()