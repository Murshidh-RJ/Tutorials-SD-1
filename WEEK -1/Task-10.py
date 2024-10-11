"""
Task 10: Temperature Conversion: 

Create a program to convert a temperature from Celsius to Fahrenheit and vice versa.

"""

# Input temperature value and type of conversion
temp = float(input("Enter the temperature value: "))
conversion_type = input("Convert to (F)ahrenheit or (C)elsius? ").lower()

# Celsius to Fahrenheit conversion
if conversion_type == 'f':
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is {fahrenheit}°F")
# Fahrenheit to Celsius conversion
elif conversion_type == 'c':
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is {celsius}°C")
else:
    print("Invalid input! Please choose 'F' or 'C'.")
