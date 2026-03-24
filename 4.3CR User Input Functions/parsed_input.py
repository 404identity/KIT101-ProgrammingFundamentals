"""
4.3CR User Input Functions
"""

__author__ = "Blake Natoli"

"""
Validates user input and outputs an int value within the constraints
"""
def input_int(prompt: str, lower: int, upper: int) -> int:
    value = None
    
    while value == None:
        try:
            value = int(input(prompt + f" ({lower} - {upper}): "))
            if value < lower or value > upper:
                value = None
                print("Answer within the constraints")
        except ValueError:
            print("Invalid answer")
            value = None

    return value

"""
Validates user input and outputs a float value within the constraints
"""
def input_float(prompt: str, lower: float, upper: float) -> float:
    value = None

    while value == None:
        try:
            value = float(input(prompt + f" ({lower} - {upper}): "))
            if value < lower or value > upper:
                value = None
                print("Answer within the constraints")
        except ValueError:
            print("Invalid answer")
            value = None
    
    return value

"""
Sanitizes and validates user input and outputs a boolean value
"""
def input_bool(prompt: str) -> bool:
    
    while True:
        value = input(prompt + " (yes/no): ")
        match value.strip().lower():
            case "y" | "yes" | "true":
                return True
            case "n" | "no" | "false":
                return False
            case _:
                print("Invalid answer")


if __name__ == "__main__":
    #All variables are initialised so code will run without error before all functions are implemented and called
    stars = -1     #user's star (between 0 and 5)
    volume = -1.0  #continuously variable speaker volume (as a value between 0 and 11)
    again = False  #do they want to try some action again?

    print("Testing input_int... the number should be saved in stars.")
    print(" - Enter '6' (should loop with error)")
    print(" - Enter '-1' (should loop with error")
    print(" - Enter '2' and it should work")
    stars = input_int("Rate the last movie you saw", 0, 5)
    print(f"Star rating: {stars}");
    print()

    print("Testing input_float... the number should be saved in volume.")
    print(" - Enter '20' (should loop with error)")
    print(" - Enter '-1' (should loop with error)")
    print(" - Enter '9.5' and it should work")
    volume = input_float("Enter amplifier volume", 0.0, 11.0)
    print(f"Volume: {volume}")
    print()

    print("Testing input_bool... the result is saved in again.")
    print(" - Extend these boolean tests by adding more messages to verify your solution!")
    print(" - Enter 'nah' and it should loop with error")
    print(" - Enter 'yes' and it should succeed")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()
    print(" - Verify that it can also read in False...")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()

    print("Tests complete...")
