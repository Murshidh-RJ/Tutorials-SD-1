'''
Task 9: Simple Interest Calculator: 

Develop a script to calculate simple interest based on user input for principal, rate of interest, and time.
'''
#task 9

principal = int(input("write the amount of pricipal you have : "))       #asking the pricipal amount from the user
rate = int(input("what is the intrest rate : "))  #asking interest rate from the user
duration = int(input("what is the time period in years ; ")) #asking duration
simple_interest = (principal*rate*duration)/100

print(" simple interest for a principal of ",principal," for a duration of ",duration," years At a rate of ",rate " is ",simple_interest,)