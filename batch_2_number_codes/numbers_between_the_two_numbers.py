# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Input 2 numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# makes the code work even if the second number input is bigger
if first_number > second_number:
    first_number, second_number = second_number, first_number

# Print the numbers between the two using for loop
for i in range(first_number + 1, second_number):
    print(i, end=' ')