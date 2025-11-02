"""
Wimbledon
Estimate: 50 minutes
Actual:   1 hour
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data

def count_champion_wins(data):
    champion_wins = {}
    countries = set()
    for row in data:
        countries.add(row[INDEX_COUNTRY])
        try:
            champion_wins[row[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_wins[row[INDEX_CHAMPION]] = 1
    return champion_wins, countries

def main():
    wimbledon_data = read_wimbledon_data(FILENAME)
    champion_wins, winning_countries = count_champion_wins(wimbledon_data)
    display_results(champion_wins, winning_countries)

def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()