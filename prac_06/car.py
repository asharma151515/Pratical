"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Class to represent a car."""

    def __init__(self, name, fuel):
        """Constructor to initialize the car's name and fuel level.

        Args:
            name (str): The name of the car.
            fuel (float): The initial amount of fuel.
        """
        self.name = name  # Instance variable for the car's name
        self.fuel = fuel  # Instance variable for fuel level
        self.odometer = 0  # Instance variable for mileage

    def __str__(self):
        """Return a readable string representation of the car."""
        return f"{self.name}, fuel={self.fuel:.2f}, odometer={self.odometer}"

    def __repr__(self):
        """Return an unambiguous string representation of the car for debugging."""
        return f"Car(name={self.name!r}, fuel={self.fuel}, odometer={self.odometer})"

    def drive(self, distance):
        """Method to simulate driving the car.

        Args:
            distance (float): The distance to drive.

        Returns:
            float: The actual distance driven based on available fuel.
        """
        fuel_needed = distance / 5  # Assume car uses 1 unit of fuel for every 5 km
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.odometer += distance
            return distance
        else:
            distance_driven = self.fuel * 5
            self.odometer += distance_driven
            self.fuel = 0  # All fuel used
            return distance_driven


