# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number from highest to lowest. Clue: sort() function

# List for the numbers
number_list = []

# Input a number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        number_list.sort(reverse=True)
        break
