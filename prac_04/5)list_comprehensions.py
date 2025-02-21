"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# For loop that creates a new list containing the first letter of each name
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension that creates a list containing the initials
# Splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# This example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# Join string method being used to create a single string from the names
print(" ".join(sorted(names)))

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# List comprehension to create a list of integers from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers that are greater than 9
greater_than_nine = [number for number in numbers if number > 9]
print(greater_than_nine)

# List comprehension and join string method to create a string of last names
# for those full names longer than 11 characters
print(", ".join([name.split()[1] for name in full_names if len(name) > 11]))  # Expected output: 'Harlem, Hendrix, Lovelace'
