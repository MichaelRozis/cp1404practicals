"""
CP1404/CP5632 Practical - Hexadecimal colour lookup
"""

COLOUR_NAME_TO_HEX = {
    "CALCIUM RED": "#e30022",
    "DODGERBLUE3": "#1874cd",
    "ELECTRIC LIME": "#ccff00",
    "HOLLYWOOD CERISE": "#f400a1",
    "HONOLULU BLUE": "#006db0",
    "MADDER LAKE": "##cc3336",
    "OPERA MAUE": "#b784a7",
    "PUMPKIN": "#ff7518",
    "AQUA": "#00ffff",
    "SLATE BLUE": "#6a5acd"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_NAME_TO_HEX.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()