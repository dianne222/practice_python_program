# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

# Loop to check even numbers from 0-100, then print the even numbers
for i in range(101):
    if i % 2 == 0:
        even_numbers.append(i)
        print(i, end = " ")