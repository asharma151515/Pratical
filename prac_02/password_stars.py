# def main():
#     password = get_password()
#     if check_min_length(password):
#         print_password_stars(password)
#     else:
#         print("Password must be at least 8 characters long.")
#
# def get_password():
#     """User to enter a password"""
#     return input("Enter your password: ")
#
# def check_min_length(password):
#     return len(password) >= 8
#
# def print_password_stars(password):
#     print('*' * len(password))
#
# if __name__ == "__main__":
#     main()



import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00  # Minimum price
MAX_PRICE = 100.00  # Maximum price
INITIAL_PRICE = 10.00
FILENAME = "stock_price_simulation.txt"  # Output file name


def simulate_stock_price(initial_price, min_price, max_price):
    """Simulate stock price changes and return final price and number of days."""
    price = initial_price
    days = 0

    while min_price <= price <= max_price:
        days += 1
        # Determine if the price goes up or down
        if random.randint(1, 2) == 1:
            # Price increases
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Price decreases
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Calculate the new price
        price *= (1 + price_change)

    return price, days


def write_to_file(prices):
    """Write the stock prices to a file."""
    with open(FILENAME, 'w') as out_file:
        # Print the starting price
        starting_price, number_of_days = prices[0]
        print(f"Starting price: ${starting_price:,.2f}", file=out_file)

        for day, price in enumerate(prices[1:], start=1):
            print(f"On day {day} price is: ${price:,.2f}", file=out_file)


# Main program execution
final_price, number_of_days = simulate_stock_price(INITIAL_PRICE, MIN_PRICE, MAX_PRICE)

# Get the starting and price readings for all days
price_history = [(INITIAL_PRICE)] + [final_price] * number_of_days  # Simplified for demonstration
write_to_file(price_history)

# Print summary information to console for user
print(f"Simulation completed over {number_of_days} days. Final price: ${final_price:,.2f}")

