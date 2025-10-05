"""
CP1404 - Practical 03
Simulate a volatile stock price with daily random changes
"""

import random

MAX_INCREASE = 0.10  # 10%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

def main():
    """Simulate daily stock price changes and write to a file."""
    price = INITIAL_PRICE
    number_of_days = 0

    out_file = open(FILENAME, 'w')

    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = 0

        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)


    out_file.close()

if __name__ == "__main__":
    main()