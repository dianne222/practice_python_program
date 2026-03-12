# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# List for the numbers
numbers_list = []
numbers_set = set()

# Input 10 numbers
for i in range(10):
    number = int(input("Enter a number: "))
    numbers_list.append(number)

print("Numbers that have duplicate:")
# Check if the number have duplicate then print it
for number in numbers_list:
    if numbers_list.count(number) > 1:
        numbers_set.add(number)

numbers_duplicate = list(numbers_set)
print(str(numbers_duplicate)[1:-1])
