import random
"""Contains functions/modules that generates random number
 for proper simulation of a temperature environment"""

# Generates random value
def randomNum():
    """Returns a Random number between the selected range"""
    return random.randint(18, 28)

# Thresholds Checker
def checkThreshhold(value):
    """Check the value to return a status msg"""
    if value <= 17:
        print("warning too cold.")
    elif value >= 28:
        print("Warning too hot")
    else:
        print("Average Temperature")

# Mode selection
def select_mode():
    """
    Select mode:
    1 → user input
    2 → random temperature test
    """
    mode = float(input("Select the type of functio 1 & 2: "))

    if mode == 1:
            value = float(input("enter temp: "))
            print(checkThreshhold(value))
    elif mode == 2:
            value = randomNum()
            print(f"Random: {value}")
            print(checkThreshhold(value))
    else:
            print("Invalid Mode")



# initialize program
if __name__ == "__main__":
    select_mode()
