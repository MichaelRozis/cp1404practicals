"""Program to determine score status."""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.uniform(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random score {random_score:.2f} is {random_result}")


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()