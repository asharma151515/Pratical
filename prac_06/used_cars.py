"""
CP1404/CP5632 Practical -
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


if __name__ == "__main__":
    main()
