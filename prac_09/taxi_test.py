"""
CP1404/CP5632 Practical 9
Demonstrate Taxi with class variable.
"""

from prac_09.taxi import Taxi
from prac_09.car import Car  # Only needed for polymorphism demo


def main():
    """Test Taxi class using class variable for consistent pricing."""
    my_taxi = Taxi("Prius 1", 100)

    print(my_taxi)

    my_taxi.start_fare()
    my_taxi.drive(40)
    print("\nAfter 40km fare:")
    print(my_taxi)
    print(f"Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(200)  # Will only drive remaining 60km due to fuel
    print("\nAfter attempting 200km (limited by fuel):")
    print(my_taxi)
    print(f"Fare: ${my_taxi.get_fare():.2f}")

    print("\nPolymorphism demonstration:")
    vehicles = [Car("Limo", 100), my_taxi, Car("Truck", 150)]
    for vehicle in vehicles:
        vehicle.drive(30)
        print(vehicle)


main()