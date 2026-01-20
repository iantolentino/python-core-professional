"""Contains a function and a formula to get the average of a list"""
temperature_samples = [13, 14, 17, 18, 20]
    
def getAverageTemp(samples):
    """Main formula to get the length of the list to divide it to the total"""
    total = 0
    for value in samples:
        total += value
    
    return total /len(samples)

def checkTemperature(value):
    """Check the value to return a status msg"""
    if value <= 17:
        return "cold"
    elif value >= 28:
        return "hot"
    else:
        return "normal"

def clampTemperature(value, minValue=17, maxValue=28):
    if value < minValue:
        return minValue
    elif value > maxValue:
        return maxValue
    else:
        return value
    
def userInput(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None
    
def validTemp(value):
    if value is None:
        return False
    if value < -50 or value > 100:
        return False
    return True
    
if __name__ == "__main__":
    samples = [21, 24, 27, 28, 30]

    avg = getAverageTemp(samples)
    print("ave: ", avg)

    
    prompt = userInput("Enter number: ")
    temp = userInput("Enter temp: ")
    if not validTemp(temp):
        print("Invalid temp")
    else:
        status = checkTemperature(temp)
        clamped = clampTemperature(temp)

        print("Status:", status)
        print("Clamp Status:", clamped)

        if status == "cold":
            print("Wear a jacket")
        else:
            print("dont go outside")