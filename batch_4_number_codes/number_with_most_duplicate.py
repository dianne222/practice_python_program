# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number with the most number of duplicate.

# List for the numbers
numbers = []

# # Input number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        numbers.sort()
        most_duplicate = max(numbers, key = numbers.count) # place the most duplicate number in the variable

        # print the most duplicate number
        print("Most number of duplicate:", most_duplicate)
        break