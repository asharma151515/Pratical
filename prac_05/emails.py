"""
Email to Name Storage
"""

def extract_name_from_email(email):
    """Extract a name from the provided email using the email's local part."""
    return email.split('@')[0].replace('.', ' ').title()                                     # Encapsulating logic in a function


def get_user_confirmation(name):
    """Get confirmation from the user about the extracted name."""
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    return confirmation in ['y', '']


def main():
    """Collect and store email-name pairs in a dictionary."""
    email_to_name = {}                  # Dictionary Data Structure

    while True:
        email = input("Email: ").strip()
        if not email:                   # Exit if input is blank
            break

        name = extract_name_from_email(email)      # Extract name using encapsulated function

        if not get_user_confirmation(name):
            name = input("Name: ").strip()        # Ask for correct name if not confirmed

        email_to_name[email] = name         # Store email and name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()

