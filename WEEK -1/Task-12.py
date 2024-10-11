'''
Task 12: Distance Converter: 

Develop a program that converts distance from meters to kilometers and miles.

'''
# Input distance in meters
meters = float(input("Enter distance in meters: "))

# Convert meters to kilometers and miles
kilometers = meters / 1000
miles = meters / 1609.34

# Output the converted values
print(f"{meters} meters is {kilometers} kilometers")
print(f"{meters} meters is {miles} miles")
