"""
Estimated time: 30 minutes
Actual time: 10 minutes
"""

class ProgrammingLanguage:
    """Class to represent a programming language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialize attributes for the ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection  # Default is False
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"


