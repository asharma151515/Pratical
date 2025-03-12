"""
Estimated time : 30 minus
Actual time : 20 minus
"""

AGE_LIMIT = 50
CURRENT_YEAR = 2022


class Guitar:
    """Guitar class for storing details of a guitar."""

    VINTAGE_AGE = 50  # Constant representing the age threshold for vintage guitars

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the current year."""
        from datetime import datetime  # Importing only as needed
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= self.VINTAGE_AGE
