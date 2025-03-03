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


def run_tests():
    """Test the ProgrammingLanguage class with sample data."""
    # Create instances of ProgrammingLanguage
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print string representations of the languages
    print(python)
    print(ruby)
    print(visual_basic)

    # Test the is_dynamic method
    print(f"{python.name} is dynamically typed: {python.is_dynamic()}")  # Expected: True
    print(f"{ruby.name} is dynamically typed: {ruby.is_dynamic()}")  # Expected: True
    print(f"{visual_basic.name} is dynamically typed: {visual_basic.is_dynamic()}")  # Expected: False


if __name__ == "__main__":
    run_tests()

