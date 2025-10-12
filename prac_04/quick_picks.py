"""Generate random 'quick pick' lottery tickets with unique numbers."""

import random

MIN= 1
MAX = 45
NUMBERS_PER_LINE = 6

def main():
    """Generate specified number of quick pick lottery tickets."""
    number_of_picks = int(input("How many quick picks?"))
    while number_of_picks <0:
        print("Invalid")
        number_of_picks = int(input("How many quick picks?"))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()