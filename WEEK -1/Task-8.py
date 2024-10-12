'''
Task 8: Unit Conversion Program: 

Implement a program that converts a given number of days into hours, minutes, and seconds.
'''
days = int(input("Please enter number of days "))
hour = days*24
print("in ",days,"there are ",hour,"hours.")

minutes = days*24*60
print("in ",days,"Days there are ",minutes,"minutes.")

seconds = days*24*60*60
print("in ",days,"days there are ",seconds,"seconds.")
