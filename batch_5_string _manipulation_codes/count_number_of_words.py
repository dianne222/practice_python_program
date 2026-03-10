# Prog07: Create a program that ask the user to input a complete statement.
# Print the number of words in the input.

# Input a statement
statement = input("Enter a statement: ")

# Separate the words in the statement
words = statement.split()

# Print the number of words
print(len(words))