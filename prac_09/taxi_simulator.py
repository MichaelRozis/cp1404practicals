"""
CP1404 Practical
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program with polymorphism."""
    taxis = [Taxi("Prius", 100.0),
             SilverServiceTaxi("Limo", 100.0, 2),
             SilverServiceTaxi("Hummer", 200.0, 4)]
    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").strip().lower()

        if choice == "q":
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            print("Thanks for using our taxi service!")
            break

        elif choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid distance")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")


main()