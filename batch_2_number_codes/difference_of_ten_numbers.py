# Prog06: Create a program that ask user to input 10 numbers.
# Print the result of the first number minus all of the remaining numbers.

# Variable where first number is added then the remaining number is subtracted
difference_of_ten_numbers = 0

# Input first number to be added to the variable
number = float(input("Enter a number: "))
difference_of_ten_numbers += number

# Input numbers to be subtracted to the variable, repeat 9 times
for i in range(9):
    number = float(input("Enter a number: "))
    difference_of_ten_numbers -= number

# Print the result
print("First number minus all remaining number is:", difference_of_ten_numbers)