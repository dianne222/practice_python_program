# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the highest number

# List for the numbers
number_list = []

# Input number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        print("Highest number:", max(number_list)) # print the highest number
        break

