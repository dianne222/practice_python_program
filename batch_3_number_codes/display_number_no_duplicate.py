# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# List for numbers
numbers = []

# Input numbers
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# checks if the number have duplicate
for num in numbers:
    if numbers.count(num) == 1:
        print(num, end=" ")

