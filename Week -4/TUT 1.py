

'''
Part 01: Guided Programming Exercises
'''
'''

Simple Exercise

    01.If Statement:

    Write an if statement to check if a number is divisible by 5. If it is, print "Divisible by 5".
'''

number = int(input("Enter the number to check if it's divisible by 5 : "))
if number%5 == 0 :

    print("Divisible by 5")



'''
    02. Else Statement:

    Create a program using if-else to determine if a person is eligible to vote (age >= 18). Print appropriate messages for both conditions.
'''
age= int(input("Enter your age : "))
if age >=18:
    print("You are elegible to vote")
else :
    print("you are not elegible to work ")





'''
    03.Elif Statement:

    Use if-elif-else to categorize a number as 'Negative', 'Zero', or 'Positive'.
'''
number=float(input("Enter the a number : "))

if number > 0:
    print("It's a positive number ")
elif number < 0 :
    print("It's a negative number ")
elif number == 0:
    print("It's Zero ")









'''
    04.Nested If-Else Statement:

    Write a nested if-else program that checks if a number is less than 10. If it is, check if it is even or odd and print the result.

'''

number =int(input("Enter a number : "))

if number <10 :
    if number%2 ==0:
        print("Its an Even Number")
    else:
        print("It's an Odd Number ")
else :
    print("it's Grater than 10 ")







    

'''
    05.If Statement:

    Create a program to check if a given year is a leap year.
'''
year = int(input("Enter the year to check if its leap or not "))

if year %4==0 or year %400==0 :
    print("It's a Leap Year")
else :
    print("It's Not a leap Year")








'''
    06.Else Statement:

    Write a program to determine whether a character entered is a vowel or consonant.
'''
character = input("Enter an alphabet letter : ")
character.upper()
if character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':
    print("It's Vowel letter")
else :
    print("It's a constant letter")

'''
if character in 'AEIOU':
    print("It's Vowel letter")
else :
    print("It's a constant letter")
'''





'''
    07.Elif Statement:

    Develop a program that categorizes a character as 'Lowercase', 'Uppercase', 'Digit', or 'Special Character'.
'''

character = input("Enter an alphabet letter : ")
if character.islower():
    print(f"{character} is a Lowercase Letter ")
elif character.isupper():
    print(f"{character} is a Upper case letter ")
elif character.isdigit():
    print(f"{character} is a Digit ")
else:
    print("its a special character ")





'''
    08. Nested If-Else Statement:
    Implement a nested if-else structure to calculate different types of discounts based on purchase amount: above 1000, 10% discount; between 500 and 1000, 5% discount; below 500, no discount.

'''

purchase_amount = int(input("Enter the amount you purshased for to obtain discount : "))
discount_for_1000= purchase_amount*(10/100)
discount_for_500_to_1000= purchase_amount*(5/100)

if purchase_amount >= 1000 :
    print(f"your discount is {discount_for_1000}, Final price is {purchase_amount-discount_for_1000}")
else:
    if purchase_amount >= 500:
        print(f"your discount is {discount_for_500_to_1000}, Final price is {purchase_amount-discount_for_500_to_1000}")

    else:
        print("For below 500 you don't get any discount buy more to save more")




































































































