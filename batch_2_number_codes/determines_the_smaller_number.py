# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# Input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Check which number is smaller then print it
if first_number < second_number:
    print("The smaller number is:", first_number)
else:
    print("The smaller number is:", second_number)