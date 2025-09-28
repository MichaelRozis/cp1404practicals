"""
Calculate total price for number of items with optional discount.
"""

# Get valid number of items
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Total price by summing item prices
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Applying 10% discount if total price > $100
if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

# Display total price with 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
