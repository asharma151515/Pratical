# CP1404/CP5632 Practical
# Enhanced code for cumulative total income program

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    # Collect income for each month
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string for input prompt
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0

    # Display the income report
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        # Using f-string for formatted output
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

# Run the main function
main()

