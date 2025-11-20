"""
CP1404 Practical
Wikipedia searcher with exception handling.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def main():
    """Search Wikipedia pages with user input until blank."""
    print("Let's search Wikipedia!")
    while True:
        search_term = input("\nEnter page title: ").strip()
        if not search_term:
            print("Thank you.")
            break

        try:
            # Use auto_suggest=False to prevent unexpected title changes
            page = wikipedia.page(search_term, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            for option in e.options:
                print(option)


if __name__ == "__main__":
    main()