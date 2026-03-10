# Prog09: Create a program that ask the user to input their fullname in incorrect casing.
# Print the input in pascal case.

# Input full name
full_name = input("Enter your full name (in incorrect casing): ")

# Print name in pascal case
print(full_name.title().replace(" ",""))