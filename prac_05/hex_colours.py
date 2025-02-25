"""
CP1404/CP5632 Practical
Hexadecimal colour codes dictionary
"""
# Constant dictionary for color names and their hex codes
COLOUR_TO_HEX = {
    "Blue": "#0000FF",
    "Red": "#FF0000",
    "Green": "#008000",
    "Yellow": "#FFFF00",
    "Black": "#000000",
    "White": "#FFFFFF",
    "Cyan": "#00FFFF",
    "Magenta": "#FF00FF",
    "Gray": "#808080",
    "Orange": "#FFA500",
    "Purple": "#800080",
    "Pink": "#FFC0CB",
}
def main():
    while True:
        colour_name = input("Enter a colour name (or leave blank to stop): ").strip()
        if not colour_name:                                    # Stop if input is blank
            break

        # Make the input case-insensitive by formatting the name properly
        colour_name_title = colour_name.title()

        try:
            # to get the hexadecimal code for the entered colour name
            hex_code = COLOUR_TO_HEX[colour_name_title]
            print(f"The hex code for {colour_name_title} is {hex_code}.")
        except KeyError:
            # Handle the case where the colour name does not exist in the dictionary
            print(f"Sorry, '{colour_name}' is not a valid colour name.")

if __name__ == "__main__":
    main()