# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# List for the numbers
numbers = []

# Input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Check if the number have duplicate then print it
for number in numbers:
    if numbers.count(number) > 1:
        print("Numbers that have duplicate:")
        print(number, end = " ")
