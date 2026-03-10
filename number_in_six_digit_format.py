# Prog02: Create a program that ask the user to input a number (0-1000). Print the
# number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# Input number 0-1000
num = int(input("Enter a number(0-1000): "))

# Check if it is 0-1000. If true, print the number in 6 digit format.
# If false, print Inavalid
if num >= 0 and num <= 1000:
    print("%06d" % (num))
else:
    print("Invalid number")