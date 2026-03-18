# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the average.

# List for the numbers
number_list = []

# Input number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)

    except ValueError:
        average = sum(number_list) / len(number_list)
        print("Average: ", average)
        break