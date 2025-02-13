"This program provides a menu interface for the scoring system."

import random

MENU_OPTIONS = {
    'G': "Get a valid score",
    'P': "Print result",
    'S': "Show stars",
    'Q': "Quit"
}

def main_menu():
    score = 0
    choice = ''
    while choice != 'Q':
        display_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell")
        else:
            print("Invalid input. Please try again.")

def display_menu():
    """Display the menu options to the user."""
    print("Menu:")
    for key, value in MENU_OPTIONS.items():
        print(f"({key}) {value}")

def determine_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score."
    elif score <= 50:
        return "Fail"
    elif score <= 65:
        return "Pass"
    elif score <= 75:
        return "Credit"
    elif score <= 85:
        return "Distinction"
    elif score <= 100:
        return "High Distinction"

def get_valid_score():
    """Prompt user for a valid score until a valid one is provided."""
    score = int(input("Enter a valid score (0-100 inclusive): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = int(input("Enter a valid score (0-100 inclusive): "))
    return score

def print_result(score):
    """Print the evaluation result based on the score."""
    result = determine_result(score)
    print("Result:", result)

def show_stars(score):
    """Display a number of stars equal to the score."""
    print("*" * score)

if __name__ == "__main__":
    main_menu()