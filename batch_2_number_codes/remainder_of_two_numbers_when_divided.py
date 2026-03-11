# Prog05: Create a program that ask user to input 2 numbers.
# Print the remainder when the first number is divided by the second number.

# Input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Get the remainder when first number is divided by the second number
remainder = first_number % second_number

# Print the remainder
print("The remainder is:", int(remainder))