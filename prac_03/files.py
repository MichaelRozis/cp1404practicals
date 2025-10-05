"""
CP1404 - Practical 03
File handling exercises for writing and reading text files
"""

def main():
    """Perform file operations for writing and reading names and numbers."""
    # 1. Write user's name to name.txt
    name = input("Enter your name: ")
    out_file = open("name.txt", "w")
    out_file.write(name)
    out_file.close()

    # 2. Read name from name.txt and print greeting
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    print(f"Hi {name}!")
    in_file.close()

    # 3. Read first two numbers from numbers.txt and print their sum
    try:
        with open("numbers.txt", "r") as in_file:
            first_number = int(in_file.readline().strip())
            second_number = int(in_file.readline().strip())
            total = first_number + second_number
            print(total)
    except FileNotFoundError:
        print("Error: numbers.txt not found")

    # 4. Read all numbers from numbers.txt and print their sum
    try:
        total = 0
        with open("numbers.txt", "r") as in_file:
            for line in in_file:
                total += int(line.strip())
            print(total)
    except FileNotFoundError:
        print("Error: numbers.txt not found")

if __name__ == "__main__":
    main()