"""
 'for loops' for printing numbers and stars.
"""

# Odd numbers, 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
print("a. Counting in 10s from 0 to 100:")
for number in range(0, 101, 10):
    print(number, end=' ')
print()

# b. Count down from 20 to 1
print("b. Counting down from 20 to 1:")
for number in range(20, 0, -1):
    print(number, end=' ')
print()

# c. Number of stars based on input
number_of_stars = int(input("Number of stars: "))
print("c. Printing stars:")
for i in range(number_of_stars):
    print('*', end='')
print()

# d. lines of increasing stars based on input
number_of_lines = int(input("Number of lines: "))
print("d. Printing lines of increasing stars:")
for line in range(1, number_of_lines + 1):
    print('*' * line)