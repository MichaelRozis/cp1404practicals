"""Password stars program."""

MIN_LENGTH = 10


def main():
    password = get_valid_password(MIN_LENGTH)
    print_asterisks(len(password))


def get_valid_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_asterisks(length, character="*"):
    print(character * length)


main()