"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria", "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)

# Input for state code
state_code = input("Enter short state: ").strip()

# Loop to check for valid state codes
while state_code != "":
    # Convert to uppercase to allow for case-insensitive input
    state_code = state_code.upper()
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
