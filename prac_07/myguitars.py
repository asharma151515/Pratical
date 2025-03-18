from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Main function to manage guitars."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)
    add_guitars(guitars, FILENAME)

def load_guitars(filename):
    """
    Load guitars from a specified CSV file.

    Args:
        filename (str): The name of the file to load guitars from.

    Returns:
        list: A list of Guitar objects.
    """
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list of guitars.")

    return guitars

def display_guitars(guitars):
    """
    Display all guitars in a readable format.

    Args:
        guitars (list): A list of Guitar objects to display.
    """
    print("\nGuitars:")
    for guitar in guitars:
        print(guitar)

def add_guitars(guitars, filename):
    """
    Prompt the user to add guitars and save them to a CSV file.

    Args:
        guitars (list): The current list of Guitar objects.
        filename (str): The name of the file to save the guitars to.
    """
    while True:
        name = input("Enter guitar name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        try:
            year = int(input("Enter year of manufacture: "))
            cost = float(input("Enter cost: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            save_guitars(guitars, filename)
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")

def save_guitars(guitars, filename):
    """
    Save the list of guitars to a specified CSV file.

    Args:
        guitars (list): A list of Guitar objects to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

if __name__ == "__main__":
    main()
