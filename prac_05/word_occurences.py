""" CP1404/CP5632 Practical
Count word occurrence in a string
"""

# word_occurrences.py

"""
Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""

def main():
    # Ask the user for a string input
    user_input = input("Enter a string: ")

    # Create a dictionary to hold word counts
    word_count = {}

    # Split the input string into words
    words = user_input.split()

    # Count the occurrences of each word using dict.get()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Extract unique words and sort them
    sorted_words = sorted(word_count.keys())

    # Find the length of the longest word for formatting
    max_length = max(len(word) for word in sorted_words)

    # Print the counts, aligned properly
    for word in sorted_words:
        print(f"{word:<{max_length}} : {word_count[word]}")  # Aligning output with f-string formatting

if __name__ == "__main__":
    main()
