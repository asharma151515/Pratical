"""
CP1404/CP5632 Practical
Car class
"""
from prac_06.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

        def drive(self, distance):
            """Drive the taxi a certain distance and accumulate fare distance."""
            distance_driven = super().drive(distance)  # Call the parent's drive method
            self.current_fare_distance += distance_driven  # Accumulate distance for fare
            return distance_driven

        def start_fare(self):
            """Reset the fare meter for a new fare."""
            self.current_fare_distance = 0

        def get_fare(self):
            """Calculate the current fare, rounded to the nearest 10 cents."""
            fare = self.price_per_km * self.current_fare_distance
            return round(fare + 0.05, 1)  # Round to the nearest 10 cents

        def __str__(self):
            """Return a string representation of the taxi, including fare details."""
            fare_amount = self.get_fare()
            return (f"{self.name}, fuel={self.fuel}, "
                    f"odo={self.odometer}, {self.current_fare_distance}km on current fare, "
                    f"${fare_amount} fare")

