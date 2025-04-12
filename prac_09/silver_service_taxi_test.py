
from prac_09.silver_service_taxi  import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)

    # Print the taxi's details
    print(taxi)

    # Get and print the fare for the current trip
    fare = taxi.get_fare()
    print(f"Fare for this trip: ${fare:.2f}")

    # Assertions to check expected outcomes
    expected_str = "Test Fancy Taxi, fuel=82, odo=18, plus flagfall of $4.50"  # Updated fuel based on driving distance
    assert str(taxi) == expected_str, f"Expected: {expected_str}, but got: {str(taxi)}"

    expected_fare = 4.50 + (18 * taxi.price_per_km)  # Calculate expected fare
    assert fare == expected_fare, f"Expected fare: ${expected_fare:.2f}, but got: ${fare:.2f}"


if __name__ == "__main__":
    main()


