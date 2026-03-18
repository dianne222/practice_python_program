# Prog01. lstrip() remove the space characters at the beginning of the string.
# Create a program that do the same functionality without using lstrip() function.

# Input name with spaces at the beginning
full_name = input("Enter your full name(with spaces at the beginning): ")

# Remove spaces at the beginning
word_list = full_name.split()
full_name = " ".join(word_list)

# Print the name
print(full_name)