# Prog04: Create a program that ask user to input a number,
# continue asking until the user input is invalid. Display the lowest number

# variable for lowest number and the count of input
lowest_number = 0
count = 0
# Input number until invalid.
while True:
    try:
        number = int(input("Enter a number: "))
        # Make the first input the lowest number then compare the rest if it is lower than the lowest
        if count == 0:
            lowest_number = number
        else:
            if number < lowest_number:
                lowest_number = number
        count += 1

    except ValueError:
        break