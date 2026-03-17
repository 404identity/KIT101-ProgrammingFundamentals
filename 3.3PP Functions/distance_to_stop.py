"""
3.3PP Functions: I chose the 'Distance Required to Stop option.
"""

__author__ = "Blake Natoli"

# Validate user input rather than just accepting random text
def get_number(prompt) -> float:
    user_input = None

    while True:
        try:
            user_input = float(input(prompt))
            break
        except ValueError:
            print("Invalid number")
    
    return user_input

# v = Initial Velocity; t = Time to react
def calculate_distance(v: float, t: float) -> float:
    FRICTION = 0.7
    GRAVITY = 9.81

    return v * t + (v**2)/(2*FRICTION*GRAVITY)

def main() -> None:
    print("Distance required to stop\n")

    print(f"Distance to stop 1: {calculate_distance(22.22, 1.75):.2f} m")
    print(f"Distance to stop 2: {calculate_distance(8.33, 3.1):.2f} m")

    v = get_number("Input initial velocity (m/s): ")
    t = get_number("Input reaction time (in seconds): ")

    print("Calculating...")
    print(f"Distance to stop: {calculate_distance(v, t):.2f} m")

if __name__ == "__main__":
    main()