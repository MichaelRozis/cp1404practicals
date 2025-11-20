"""
CP1404/CP5632 Practical
Testing code using assert and doctest
All TODOs
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence
    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("what if multiple  !!")
    'What if multiple  !!.'
    """
    if not phrase:  # handle empty string
        return "."
    phrase = phrase.strip().capitalize()
    phrase = phrase.rstrip(".")
    return phrase + "."


def run_tests():
    """Run all assert tests."""
    # repeat_string tests
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Car odometer test
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    # TODO 2: Car fuel tests
    # Default fuel = 0
    car = Car()
    assert car.fuel == 0, "Car does not set default fuel to 0"

    # Fuel passed to constructor
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set provided fuel correctly"


run_tests()

# TODO 3: Run doctests
doctest.testmod(verbose=True)