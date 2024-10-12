'''
Task 6 :Basic Arithmetic Calculator: 

Create a simple calculator that performs addition, subtraction, multiplication, and division based on user inputs.
'''

num_1 = int(input("please enter 1st number : "))
num_2 = int(input("please enter the 2nd number : "))
operater=  input("Please enter the operation to be performed(+,-,*,/) : ")

if operater == '+':
  sum = num_1 + num_2
  print("The sum of two numbers are ",sum,)
elif operater == '*':
  mult = num_1 * num_2
  print("The multiplication of two numbers are ",mult,)
elif operater == '-' : 
  subst = num_1 - num_2
  print("the substraction of the two numbers are ",subst,)
elif operater == '/' :
  div = num_1 / num_2
  print("the division of the two numbers are ",div)
else:
  print("enter a valid operation")
