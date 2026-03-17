"""
3.2PP Fill in the Blanks: Tour de France Wrap-up
"""

__author__ = "Blake Natoli"

# Makes sure the user's input is a number
def getTime(prompt: str) -> float:
    time = None

    while True:
        try:
            time = float(input(prompt))
            break
        except ValueError:
            print("Invalid number")
    
    return time

def main() -> None:
    print("Tour de France 2025 - Final Standings\n")

    first_place: str = input("Enter name of the rider in first place: ")
    country_1: str = input(f"What country is {first_place} from? ")

    second_place: str = input("Enter the name of the rider in second place: ")
    country_2: str = input(f"What country is {second_place} from? ")

    time_1: float = getTime(f"Enter the time of {first_place}: ")
    time_2 = None

    while True:
        time_2 = getTime(f"Enter the time of {second_place}: ")
        if time_2 <= time_1:
            print(f"{second_place} should have a higher time than {first_place}")
        elif time_2 > time_1:
            break
    
    margin = time_2 - time_1

    print(f"{first_place} of {country_1} has claimed victory in the 2025 Tour de France!")
    print(f"They beat {second_place} of {country_2} by just {margin:.2f} hours.")
    print(f"With a total time of {time_1}, {first_place} has made cycling history!")

if __name__ == "__main__":
    main()