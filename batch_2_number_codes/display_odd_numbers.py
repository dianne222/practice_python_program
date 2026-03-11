# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Variable for number that is being checked if odd or not
number = 0

# Checks the numbers 0-100 if odd or not, if yes print it. Using while loop
while number <= 100:
    if number % 2 != 0:
        print(number, end=' ')
    number += 1