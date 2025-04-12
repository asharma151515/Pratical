"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.car import Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # Class variable for the fare per kilometer

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on the parent class Car."""
        super().__init__(name, fuel)  # Call the parent class (Car) initializer
        self.current_fare_distance = 0  # Initialize current fare distance

    def __str__(self):
        """Return a string representation of the Taxi including fare details."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip rounded to the nearest 10 cents."""
        fare = round(self.price_per_km * self.current_fare_distance, 1)  # Calculate the fare
        return fare  # Return the calculated fare

    def start_fare(self):
        """Begin a new fare by resetting the current fare distance."""
        self.current_fare_distance = 0  # Reset the fare distance to zero

    def drive(self, distance):
        """Drive the Taxi, extending the parent Car's drive functionality to include fare distance."""
        distance_driven = super().drive(distance)  # Get distance driven from parent class
        self.current_fare_distance += distance_driven  # Update current fare distance
        return distance_driven  # Return the distance driven

