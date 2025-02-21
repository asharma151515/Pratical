# CP1404/CP5632 Practical
# Data file -> subject_reader.py

FILENAME = "subject_data.txt"

def main():
    """Main function to load and display subject data."""
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data = []  # Initialize an empty list to store the subject data
    try:
        with open(FILENAME, 'r') as input_file:  # Use 'with' to ensure the file is closed properly
            for line in input_file:
                line = line.strip()  # Remove the newline character
                if line:  # Check if the line is not empty
                    parts = line.split(',')  # Split the line into its parts
                    parts[2] = int(parts[2])  # Convert the number of students to an integer
                    data.append(parts)  # Add the parts to the data list
    except FileNotFoundError:
        print(f"Error: The file {FILENAME} was not found.")
    except ValueError:
        print("Error: There was an issue converting the number of students to an integer.")
    return data  # Return the collected data

def display_subject_details(data):
    """Display each subject's details."""
    print("\nSubject Details:\n----------------")
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

# Run the main function
if __name__ == "__main__":
    main()