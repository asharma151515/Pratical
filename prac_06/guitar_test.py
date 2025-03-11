"""
Estimated time : 30 minutes
Actual time : 20 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Test the Guitar class methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}.")  # Expected: 100

    guitar2 = Guitar("Another Guitar", 2013, 1200.00)
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}.")  # Expected: 9

    # is_vintage method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}.")  # Expected: True
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}.")  # Expected: False

if __name__ == "__main__":
    main()
