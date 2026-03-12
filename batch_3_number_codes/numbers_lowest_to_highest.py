# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number from lowest to highest. Clue: sort() function

# Input number until invalid input
while True:
    try:
        number = int(input("Enter a number: "))

    except ValueError:
        break