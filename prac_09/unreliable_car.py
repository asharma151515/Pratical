from prac_06.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that randomly breaks down."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but randomly break down."""
        if random.randint(1, 100) <= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0

    def __str__(self):
        """Return a string representation of the UnreliableCar."""
        return f"{super().__str__()} (Reliability: {self.reliability}%)"
