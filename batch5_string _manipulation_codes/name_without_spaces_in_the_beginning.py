# Prog01: Create a program that ask the user to input their fullname with several space
# characters at the beginning. Print the input without the spaces in the beginning.

# Input fullname
full_name = input("Enter your full name: ")

# Output without spaces in the beginning
print(full_name.lstrip())
