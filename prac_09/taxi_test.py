"""The taxi_test.py file creates a Taxi object, drives it a certain distance, prints the details and current fare,
restarts the meter, drives it again, and prints the details and current fare."""

from taxi import Taxi


def test_taxi():
    """Test taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

