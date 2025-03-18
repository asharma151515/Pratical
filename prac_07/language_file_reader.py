""" CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # File format is like: Language,Typing,Reflection,Year
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()

        # All other lines are language data
        for line in in_file:
            parts = line.strip().split(',')

            # Check if parts has enough elements to create a ProgrammingLanguage object
            if len(parts) >= 5:  # Updated to check for 5 elements
                reflection = parts[2] == "Yes"
                # Construct a ProgrammingLanguage object using the elements
                language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), parts[4])
                languages.append(language)
            else:
                print(f"Issue with line: {line}. Skipping this line.")

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()