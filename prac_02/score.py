"""
Program to evaluate a user's score and categorize it.
"""


def main():
    """Main function to get the user's score and print the evaluation result."""
    score = float(input("Enter your score (0-100): "))
    result = evaluate_score(score)
    print(result)


def evaluate_score(score):
    """Evaluate the score and return a category.

    Args:
        score (float): The score to evaluate.

    Returns:
        str: A message categorizing the score.
    """
    if score < 0 or score > 100:
        return "Invalid score!"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()