# CP1404/CP5632 Practical
# Lists "warm-up"

# Initialize a list with specified numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

# Evaluate the values of specific expressions
print("First element:", numbers[0])        # First element
print("Last element:", numbers[-1])         # Last element
print("Fourth element:", numbers[3])        # Fourth element
print("All except first two:", numbers[:-1]) # All elements except the last
print("Slicing element at index 3 to 4:", numbers[3:4]) # Slicing the list
print("Is 5 in numbers?", 5 in numbers)    # Check for presence of 5
print("Is 7 in numbers?", 7 in numbers)    # Check for presence of 7
print("Is '3' in numbers?", "3" in numbers) # Check for presence of string '3'

# Modify the list as specified
numbers[0] = "ten"  # Change the first element to "ten"
numbers[-1] = 1     # Change the last element to 1

# Output all elements except the first two
print("Elements excluding first two:", numbers[2:]) # Display elements after the first two

# Check if 9 is still in the numbers list
print("Is 9 still in numbers?", 9 in numbers) # Check presence of 9

