import random

# Constants for the quick pick configuration
NUMBER_OF_NUMBERS = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

def generate_quick_pick():
    """Generate a single quick pick with non-repeating random numbers."""
    quick_pick = random.sample(range(LOWEST_NUMBER, HIGHEST_NUMBER + 1), NUMBER_OF_NUMBERS)
    return sorted(quick_pick)

def main():
    """Main function to run the quick picks program."""
    while True:
        try:
            # Get the number of quick picks from the user
            number_of_picks = int(input("How many quick picks? "))
            if number_of_picks < 1:
                print("Please enter a number greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate and print the requested number of quick picks
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2d}" for number in quick_pick))

if __name__ == '__main__':
    main()
