"""
CP1404 - Practical 03
String formatting
"""

def main():
    """Format strings using f-strings for guitar details and power table."""
    # Task 1: Format guitar details
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.9
    print(f"{year} {name} for about ${cost:,.0f}!")

    # Task 2: Generate power table for 2^0 to 2^10
    for exponent in range(11):
        result = 2 ** exponent
        print(f"2 ^{exponent:>2} is {result:>4}")

if __name__ == "__main__":
    main()