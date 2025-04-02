from prac_09.silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Test silver service taxi class."""
    my_taxi = SilverServiceTaxi("Hummer", 100, 2)
    print(my_taxi)
    my_taxi.drive(18)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


test_silver_service_taxi()
