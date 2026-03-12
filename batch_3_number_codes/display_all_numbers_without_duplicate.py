# Prog02: Create a program that ask user to input 10 numbers. Display all numbers.
# For numbers with duplicate, display only the first entry.

# List for the numbers
numbers_list = []

# Input 10 numbers using for loop
for i in range(10):
    number = int(input("Enter a number: "))
    numbers_list.append(number)

# change the list into set then back to list
numbers_set = set(numbers_list)
numbers_list = list(numbers_list)

