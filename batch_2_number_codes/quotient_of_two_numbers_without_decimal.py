# Prog04: Create a program that ask user to input 2 numbers.
# Print the quotient of the two numbers without the decimal point

# Input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# divide the two numbers with floor division and then print the quotient
quotient = first_number // second_number
print("The quotient is:", int(quotient))