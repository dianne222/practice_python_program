# Prog08: Create a program that ask user to input 10 numbers.
# Print how many are odd numbers.

# Variable that counts odd numbers
odd_numbers_count = 0

# Input number then check if odd or not, if odd the count of odd increases. loop 10 times
for i in range(10):
    number = float(input("Enter a number: "))
    if number % 2 != 0:
        odd_numbers_count += 1

# print the count of odd numbers
print("Odd numbers count:", odd_numbers_count)
