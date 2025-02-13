def main():
    """Main function to handle the temperature conversion process."""
    # Get user input for temperature and conversion choice
    temp = float(input("Enter the temperature: "))
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()

    # Call the appropriate function based on the user's choice
    if choice == 'C':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}F is {converted_temp:.2f}C.")
    elif choice == 'F':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}C is {converted_temp:.2f}F.")
    else:
        print("Invalid choice. Please select 'C' or 'F'.")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    main()