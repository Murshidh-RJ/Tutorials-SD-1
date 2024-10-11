#Task 1: Basic Arithmetic Operations
#Open IDLE and select the Python Shell.
#Type and execute basic arithmetic operations, like 3 + 4, 5 * 6, and 10 / 2.
#Observe and note the results displayed in the shell.

print(3+4)
print(5*6)
print(10/2)



x=5
name="Alice"
print(x)
print(name)

#Task3

age = input("Enter your age : ")
age = int(age)
print(f"your ate {age} years old.")

#Task 4
first_name = "Jhon"
second_name = "Doe"
full_name = first_name+" "+last_name
print(full_name)

#Task 5
print("hello
print("Hello")


#task6

num_1 = int(input("please enter 1st number : "))
num_2 = int(input("please enter the 2nd number : "))

sum = num_1 + num_2
print("The sum of the rwon numbers are ",sum,)

mult = num_1 * num_2
print("The multiplication of two numbers are ",mult,)

subst = num_1 - num_2
print("the substraction of the two numbers are ",subst,)

div = num_1 / num_2
print("the division of the two numbers are ",div)


#task 7

name = input("please enter your name :")  #asking user name as a input
age = input("please enter your age : ")  #asking age as input
fav_clr = input("what is your Favorite color : ")  #asking favorite color
print("Hello ",name,". You are ",age," Years old. Your favorite color is ",fav_clr,".")

#task 8

days = int(input("Please enter number of days "))
hour = days*24
print("in ",days,"there are ",hour,"hours.")

minutes = days*24*60
print("in ",days,"Days there are ",minutes,"minutes.")

seconds = days*24*60*60
print("in ",days,"days there are ",seconds,"seconds.")

#task 9

principal = int(input("write the amount of pricipal you have : "))       #asking the pricipal amount from the user
rate = int(input("what is the intrest rate : "))  #asking interest rate from the user
duration = int(input("what is the time period in years ; ")) #asking duration
simple_interest = (principal*rate*duration)/100

print(" simple interest for a principal of ",principal," for a duration of ",duration," years At a rate of ",rate " is ",simple_interest,)
