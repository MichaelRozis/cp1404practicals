"""
CP1404 - Practical 03
Get a valid integer from the user with exception handling
"""

def main():
    """Prompt for a valid integer and handle invalid input."""
    is_finished = False
    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True  # Exit loop on successful integer input
        except ValueError:  # Catch invalid integer input
            print("Please enter a valid integer.")
    print(f"Valid result is: {result}")

if __name__ == "__main__":
    main()