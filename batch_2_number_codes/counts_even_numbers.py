# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Variable for counting even numbers
even_numbers = 0

# Input numbers then check if it's even number, if yes, increase the count of even number repeat 10 times
for i in range(10):
    number = float(input("Enter a number: "))
    if number % 2 == 0:
        even_numbers += 1

# Print the count of even numbers
print("Even numbers count:", even_numbers)