"""
CP1404 Practical - Test SilverServiceTaxi with assert statements
Includes the exact 18km trip example from the practical
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi behaviour including inheritance of rounding."""
    # Test basic luxury taxi
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    assert str(hummer) == "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"

    # Test the exact example from the practical
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)

    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18km trip: ${fare:.2f}")
    assert fare == 48.80, f"Expected 48.80 but got {fare}"  # Must be exactly 48.80 after rounding

    print("All SilverServiceTaxi tests passed!")


main()