# Prog07: Create a program that ask user to input 10 numbers.
# Print the sum of all the numbers.

# variable where the ten numbers is added
sum_of_ten_numbers = 0

# Input number and add it to the variable, loop 10 times
for i in range(10):
    number = float(input("Enter a number: "))
    sum_of_ten_numbers += number

# Print the sum of 10 numbers
print("The sum of ten numbers is:", sum_of_ten_numbers)