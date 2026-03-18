# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the average.

# Input number until invalid
while True:
    try:
        number = int(input("Enter a number: "))

    except ValueError:
        break