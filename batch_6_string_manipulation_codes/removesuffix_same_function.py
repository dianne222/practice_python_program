# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter.
# Create a program that do the same functionality without using removesuffix() function.

# List of files
files = ["python.txt", "java.txt", "c++.txt", "html"]
file_name = []

# Code that can replace removesuffix() function
for file in files:
    if file.endswith(".txt"):
        file_name.append(file.replace(".txt", ""))
    else:
        file_name.append(file)

# Print the result
print(str(file_name)[1:-1])