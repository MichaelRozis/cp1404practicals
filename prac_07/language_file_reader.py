"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Read languages from file, create objects, and display them."""
    languages = []
    in_file = open('languages.csv', 'r')

    # Skip header
    in_file.readline()

    # Process each data line
    for line in in_file:
        parts = line.strip().split(',')

        # Convert string flags to Boolean
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[3] == "Yes"

        # Create object and store
        language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))
        languages.append(language)

    in_file.close()

    # Display all languages
    for language in languages:
        print(language)


main()