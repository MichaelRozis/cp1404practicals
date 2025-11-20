"""
CP1404/CP5632 Practical
Demonstrate Taxi inheritance and polymorphism.
"""

from prac_09.taxi import Taxi


def main():
    """Test the Taxi class with realistic usage and demonstrate polymorphism."""
    # Create a taxi with the exact signature required by the provided class
    my_taxi = Taxi("Prius 1", 100, 1.23)

    print(my_taxi)
    print()

    # First fare
    my_taxi.start_fare()
    my_taxi.drive(40)
    print("After 40km fare:")
    print(my_taxi)
    print(f"Fare: ${my_taxi.get_fare():.2f}")
    print()

    # Second fare - runs out of fuel part-way
    my_taxi.start_fare()
    my_taxi.drive(200)   # Only 60 fuel left, so only drives 60km
    print("After attempting 200km fare (limited by fuel):")
    print(my_taxi)
    print(f"Fare: ${my_taxi.get_fare():.2f}")
    print()

    # Polymorphism demonstration
    print("Polymorphism - list of mixed Car and Taxi objects:")
    from prac_09.car import Car
    vehicles = [Car("Limo", 100), my_taxi, Car("Truck", 150)]
    for vehicle in vehicles:
        vehicle.drive(30)
        print(vehicle)


main()
