
"""Contains the functions to convert Celsius to Fahrenheit"""

# Celcius to Fahrenheit
def celsius_to_fahrenheit(value):
    converted = (value *1.8)+32
    return converted

# Fahrenheit to Celsius
def fahrenheit_to_celsius(value):
    converted = (value - 32)*5/9
    return converted

# Testing
if __name__ == "__main__":
    celsius = float(input("Input Celsius: "))
    c_formula = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C → {c_formula}")

    fahrenheit = float(input("Input Fahrenheit: "))
    f_formula = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F → {f_formula}")
