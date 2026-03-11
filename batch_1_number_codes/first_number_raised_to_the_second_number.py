# Prog06: Create a program that ask user to input 2 numbers.
# Print the result when the first number is raised to the second number.

# Input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# first number raised to second then print the result
power_result = first_number ** second_number
print(f"{first_number} raised to the {second_number} is:", power_result)