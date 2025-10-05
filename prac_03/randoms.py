"""
CP1404 - Practical 03
Random number exercises using the random module
"""

import random

def main():
    """Generate and analyze random numbers using random module functions."""
    # Line 1: random.randint(5, 20)
    # Observed: A random integer between 5 and 20 (e.g., 12, 15, 20)
    # Smallest possible: 5
    # Largest possible: 20

    # Line 2: random.randrange(3, 10, 2)
    # Observed: A random odd integer between 3 and 9 (e.g., 3, 5, 7, 9)
    # Smallest possible: 3
    # Largest possible: 9
    # Could it produce 4? No, because step=2 starts at 3, giving only odd numbers (3, 5, 7, 9)

    # Line 3: random.uniform(2.5, 5.5)
    # Observed: A random float between 2.5 and 5.5 (e.g., 3.728, 4.912)
    # Smallest possible: 2.5
    # Largest possible: 5.5

    # Generate a random number between 1 and 100 inclusive
    random_number = random.randint(1, 100)
    print(f"Random number between 1 and 100: {random_number}")

if __name__ == "__main__":
    main()