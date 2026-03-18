# Prog03. upper() converts all characters of the string into upper case.
# Create a program that do the same functionality without using upper() function.

# list for characters
characters = []

# Input full name in lower case
full_name = input("Enter your full name(in lower case): ")

# turns the characters into upper case
for i in full_name:
    if 'a' <= i <= 'z':
        characters.append(ord(i) - 32) #converts the lower case letter to upper case using ASCII
    elif 'A' <= i <= 'Z':
        characters.append(i)




print(full_name)