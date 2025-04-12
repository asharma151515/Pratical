from unreliable_car import UnreliableCar


def test_unreliable_car():
    """Test unreliable car class."""
    my_car = UnreliableCar("DeLorean", 100, 90)
    print(my_car)
    distance = my_car.drive(5)
    print(f"The car drove {distance}km")
    distance = my_car.drive(10)
    print(f"The car drove {distance}km")


test_unreliable_car()
