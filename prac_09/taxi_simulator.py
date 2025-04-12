from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Taxi simulator program.

    This function simulates a taxi service, allowing users to choose a taxi, drive, and track the bill.
    """
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")

    choice = ""
    while choice != "Q":
        choice = input(">>> ").upper()

        if choice == "Q":
            print(f"Total trip cost: ${bill_to_date:.2f}")
        elif choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi choice. Please enter a valid number.")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                try:
                    distance = int(input("Drive how far? "))
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    bill_to_date += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid distance. Please enter a number.")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

        print("q)uit, c)hoose taxi, d)rive")  # Print the menu again

main()