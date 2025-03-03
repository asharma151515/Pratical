"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


from car import Car

def main():
    # Collect user input for creating Car objects
    car_name = input("Enter the name of the car: ")
    initial_fuel = float(input("Enter the initial fuel amount: "))

    # Create a new Car object
    my_car = Car(car_name, initial_fuel)

    print(my_car)  # Print the car object using the __str__ method

    # Example of driving the car
    while True:
        try:
            distance = float(input("Enter distance to drive (or -1 to quit): "))
            if distance < 0:
                print("Exiting the driving simulator.")
                break
            distance_driven = my_car.drive(distance)
            print(f"Driven distance: {distance_driven} km")
            print(my_car)  # Print updated car object
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
