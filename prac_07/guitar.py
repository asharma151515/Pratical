class Guitar:
    """Represent a guitar with various attributes."""

    VINTAGE_YEAR = 50  # A guitar is vintage if it's over 50 years old

    def __init__(self, name, year, cost):
        """
        Initialize a new Guitar instance.

        Args:
            name (str): The name of the guitar.
            year (int): The year the guitar was made.
            cost (float): The cost of the guitar.
        """
        self.name = name
        self.year = year
        self.cost = cost

    def is_vintage(self):
        """
        Determine if this guitar is considered vintage.

        Returns:
            bool: True if the guitar is vintage, False otherwise.
        """
        current_year = 2023  # Update this value dynamically if needed
        return (current_year - self.year) > self.VINTAGE_YEAR

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"
