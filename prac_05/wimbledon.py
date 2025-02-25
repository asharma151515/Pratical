"""
CP1404/CP5632 Practical
Wimbledon data-reading, processing and displaying
"""

FILENAME = "wimbledon.csv"

def main():
    """Read data file and print details about Wimbledon champions and countries."""
    try:
        records, headers = load_records(FILENAME)
        if records:
            champion_to_count, countries = process_records(records, headers)
            display_results(champion_to_count, countries)
    except Exception as e:
        print(f"An error occurred: {e}")

def process_records(records, headers):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_index = headers.index("Champion")
    country_index = headers.index("Country")

    champion_to_count = {}
    countries = set()

    for record in records:
        countries.add(record[country_index])
        champion_name = record[champion_index]

        # Use dict.get() to increment counts
        champion_to_count[champion_name] = champion_to_count.get(champion_name, 0) + 1

    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def load_records(filename):
    """Load records from file in list of lists form."""
    records = []
    headers = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            headers = in_file.readline().strip().split(",")  # Store headers
            for line in in_file:
                parts = line.strip().split(",")
                records.append(parts)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading records: {e}")

    return records, headers

if __name__ == "__main__":
    main()
