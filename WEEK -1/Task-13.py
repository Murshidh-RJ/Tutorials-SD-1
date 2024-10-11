'''
Task 13: BMI Calculator: 

Implement a Body Mass Index (BMI) calculator that takes weight and height as inputs and calculates BMI.

'''
# Input weight (in kg) and height (in meters)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Output the BMI
print("Your BMI is:", bmi)
