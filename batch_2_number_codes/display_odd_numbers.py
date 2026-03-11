# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Loop to check odd numbers from 0-100, then print the odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i, end = " ")