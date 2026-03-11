# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# Loop to check numbers that are not ending in zero, and then print
for i in range(101):
    if i % 10 != 0:
        print(i, end = " ")