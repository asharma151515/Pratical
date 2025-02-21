# CP1404 List Exercises

def main():
    """Main function to perform basic list operations."""
    numbers = []  # Initialize an empty list to store numbers

    # Prompt user for 5 numbers
    for i in range(5):
        number = int(input(f"Number {i + 1}: "))  # Get a number from the user and store as integer
        numbers.append(number)

    # Calculate required details
    first_number = numbers[0]
    last_number = numbers[-1]
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0  # Avoid division by zero

    # Output information about the numbers
    print(f"\nThe first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum of the numbers is {total}")
    print(f"The average of the numbers is {average}")

    # 2. Woefully inadequate security checker
    authorized_users = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]
    # Ask the user for their username
    username = input("\nEnter your username: ")

    # Checking if the username in the authorized users list
    if username in authorized_users:
        print("Access granted")
    else:
        print("Access denied")

# Run the main function
if __name__ == "__main__":
    main()