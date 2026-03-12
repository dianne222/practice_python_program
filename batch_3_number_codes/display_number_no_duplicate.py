# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# List for numbers
numbers = []

# Input numbers
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

# checks if the number have duplicate
for number in numbers:
    if numbers.count(number) == 1:
        print(num, end=" ")

