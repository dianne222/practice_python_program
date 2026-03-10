# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# Input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Print the bigger number by comparing
if first_number > second_number:
    print("The bigger number is:", first_number)
else:
    print("The bigger number is:", second_number)