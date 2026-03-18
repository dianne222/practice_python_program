# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number with the most number of duplicate.

# List for the numbers
numbers = []
duplicates = {}

# Input number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)

    except ValueError:
        numbers.sort()
        for i in numbers:
            duplicates[i] = numbers.count(i)
        most_duplicate = max(duplicates, key = duplicates.get)
        print("Most duplicate number:", most_duplicate)

        break