"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Initial sales input
sales = float(input("Enter sales: $"))
while sales >=0:
    #Bonus depending on sales
    if sales < 1000:
        bonus = sales * 0.10 #The 10% bonus for < 1000
    else:
        bonus = sales * 0.15 #The 15% bonus for >= 1000
    print(f"bonus: ${bonus:.2f}")
    # New sales entry
    sales = float(input("Enter sales: $"))
print("program ended")
