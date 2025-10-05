"""
CP1404 - Practical 03
Demonstrate exception handling for division with input validation
"""

def main():
    """Prompt for numerator and denominator, perform division, and handle exceptions."""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        # Question 1: When will a ValueError occur?
        # A ValueError occurs if the input for numerator or denominator cannot be converted to an integer,
        # e.g., entering "abc" or "seven" instead of a number like "5".

        # Question 2: When will a ZeroDivisionError occur?
        # A ZeroDivisionError occurs if the denominator is 0,
        # since dividing any number by 0 is mathematically undefined.

        # Question 3: Could you change the code to avoid the possibility of a ZeroDivisionError?
        # Yes, by checking if the denominator is not zero before performing the division.
        # This uses the "Look Before You Leap" (LBYL) approach to prevent the error.

        # Modified code to avoid ZeroDivisionError
        if denominator != 0:
            fraction = numerator / denominator
            print(fraction)
        else:
            print("Cannot divide by zero!")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except:
        print("Some other exception happened")
    print("Finished.")

if __name__ == "__main__":
    main()