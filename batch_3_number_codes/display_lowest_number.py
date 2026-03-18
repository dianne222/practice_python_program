# Prog04: Create a program that ask user to input a number,
# continue asking until the user input is invalid. Display the lowest number

# list for the number
number_list = []

# Input number until invalid.
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        print("Lowest number:", min(number_list))
        break