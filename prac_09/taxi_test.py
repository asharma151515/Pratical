"""The taxi_test.py file creates a Taxi object, drives it a certain distance, prints the details and current fare,
restarts the meter, drives it again, and prints the details and current fare."""

from taxi import Taxi


def main():
    """create a new taxi object."""
    my_taxi = Taxi("Prius 1", 100)

    # drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare) and then drive the car 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Print the details and the current fare again
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
