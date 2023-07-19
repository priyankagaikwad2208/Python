# print("I am priyanka")
# print("o----")
# print('||||')
# print("*" * 10)

# variables

# price=10
# price=20
# rating=4.6
# name="priya"
# is_published = False
# print(price,',',rating,',',name,'.')
#
# name= 'joan smith'
# age=20
# is_new= True
#
#
# name=input("what is your name? ")
# print("hi ", name)
# color= input('what is your favorite color ?')
# print(name + " likes "+ color)

# type conversion
# birth_year= input("birth year: ")
# age= 2022- int(birth_year)
# print(age)

# weight_lbs= int(input("weight (lbs) : "))
# weight_kg= (weight_lbs)* 0.45
# print(weight_kg)

# string

# course="python's course for beginners"
# print(course)

# x='''hi priya,
# welcome to college
#
# thank you for coming
# bye'''
# print(x)
# print(x[:5])


# formatted strings

# first= "priya"
# last =" gaikwad"
# message =first + ' [' + last +'] is a coder'
# m = first + last +" is a coder"
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(m)
# print(msg)

# string method

# course= "python for beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('o'))
# print(course.replace('beginners','absolute beginners'))
#
# print("python" in course)


# arithmetic operator

# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10%3)
# print(10**3)
# print(10//3)
# #
# x=10
# x=x+3
# print(x)
#
# x+=3
# print(x)

# operator precedence

# x=10+3*2
# print(x)
#
# x=(10+3)*2
# print(x)
#
# x=2**1*5
# print(x)
#
# x=2**5
# print(x)
#
# x= (2+3)*10-3
# print(x)

# math functions

# x=2.9
# print(round(x))
#
# x=2.1
# print(round(x))
#
# x= -2.9
# print(abs(-2.9))
#
# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))

# for more math function search on google 'python 3 math module'

# if statement

# is_hot=False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# else:
#     print("It's a cold day")
#     print("wear warm cloths")
#
#
# is_hot=False
# is_cold=False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("wear warm cloths")
# else:
#     print("enjoy your days!")
#
# price= 1000000
# has_good_credit= True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')

# Logical operator
# and operator= both condition true
# or operator= at least one condition true
# not=  it inverse the boolean value

# has_high_income=True
# has_good_credit=True
# if has_high_income and has_good_credit:
#     print("eligble for loan ")
#
# has_high_income=True
# has_good_credit=False
# if has_high_income or has_good_credit:
#     print("eligble for loan ")

# has_high_income=True
# has_good_credit=False
# if has_high_income and not  has_good_credit:
#     print("eligble for loan ")

# comparision operator

# temp=30
# if temp>30:
#     print("It's a hot day")
# else :
#     print("It's not a hot day")
#
# name=str(input("enter your name : "))
# if len(name)<3:
#     print("name must be at least 3 characters")
# elif len(name)>10:
#     print("name can be maximum of 10 characters")
# else:
#     print("name looks good!")

# project: weight converter


# weight=int(input("weight: "))
# unit= input('(L)bs or (K)g: ')
# if unit == "L":
#     converted=weight*0.45
#     print(f'you are {converted} kg')
# else:
#     converted=weight//0.45
#     print(f'you are {converted} ponds')
#
# while loop

# i=1
# while i<=5:
#     print(i)
#     i=i+1
# print("done")

# i=1
# while i<=5:
#     print("*"* i)
#     i=i+1
# print("done")

# guessing game

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess= int(input("guess: "))
#     guess_count +=1
#     if guess==secret_number:
#         print("you won!")
#         break
# else:
#     print("sorry,you failed!")

# a=5
# i=1
# while i<=3:
#     guess=int(input("Guess: "))
#     i+=1
#     if guess==a:
#         print("you win!")
#         break
# else:
#     print("sorry, you failed!")


# car game

# for loop

# a= ("priya", "shivaji","gaikwad")
# for i in a:
#     print(i)
#
# for i in ["priya","shivaji","gaikwad"]:
#     print(i)
#
# for i in range(10):
#     print(i)

# for i in range(5,12):
#     print(i)

# prices= (10,20,30)
# total=0
# for price in prices:
#     total=total+price
# print(f"total: {total}")

# nested loop

# for x in range(3):
#     for y in range(3):
#         print(f'({x},{y})')

# number=[5,2,2,5,2]
# for a in number:
#     print('priya ' * a )


# list

# names=["priya","ram","shyam","radha","shivaji"]
# print(names)
# print(names[2])
# print(names[-1])
# print(names[2:4])
# print(names[2:])
# print(names[:2])
# print(names[:])
# names[3]="rani"
# print(names)

# write a program to find the largest number in a list

# numbers = [3,5,9,6,5,10,15,14,12]
# max = numbers[0]
# for number in numbers:
#     if number>max:
#         max=number
#  print(max)

# numbers =[5,7,1,2,3]
# print(numbers)
# numbers.append(12)
# print(numbers)
#
# # numbers.insert(0,9)
# print(numbers)
#
# # numbers.remove(1)
# print(numbers)
#
# # numbers.pop()
# print(numbers)
#
# print(numbers.index(3))
# print(numbers)
#
# print (numbers.count(1))
#
# (numbers.sort())
# print(numbers)


# # creat own calculator
# print("select an operation to perform")
# print("1. Add")
# print("2.Substact")
# print("3. Multiply")
# print("4. Division")
#
# operation= input()
#

# if operation == "1":
#     num1 = (input("Enter First number : "))
#     num2 = (input("Enter Second number :"))
#     print("The sum is :" + str(int(num1) + int(num2)))
# elif operation == "2":
#     num1 = int (input("Enter first number :"))
#     num2 = int (input("Enter second number :"))
#     print("The substraction is :" + str(int(num1) - int(num2)))
# elif operation == "3":
#     num1 = int (input("Enter first number :"))
#     num2 = int (input("Enter second number :"))
#     print("The multiplication  is :" + str(int(num1) * int(num2)))
# elif operation == "4":
#     num1 = int (input("Enter first number :"))
#     num2 = int (input("Enter second number :"))
#     print("The Division  is :" + str(int(num1) / int(num2)))
# else:
#     print("Invalid Entry")

# Tuples
# tupels are unmutatable

# numbers=(1,2,3)
# print(numbers[0])
#
# #unpacking of tuple
#
# cordinates = (1,2,3)
# x= cordinates[0]
# y= cordinates[1]
# z= cordinates[2]
# p=x*y*z
# print(p)

# Dictionaries

# name: priya
# Email: gaikwadpriyanka7560@gamil.com
# phone:9552250591

# customer={
#     "Name" : "Priyanka Gaikwad",
#     "Age": 22,
#     "is_verified": True
# }
# print(customer["Name"])
# print(customer.get("birthdate", "Aug 22 2000"))
# customer["birthdate"] = "22 8 2000"
# print(customer["birthdate"])
#
# #emoji Converter
#
# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)" : "😁",
#     ":(" : "😌"
# }
# outward =""
# for word in words:
#     outward += emojis.get(word,word +" ")
# print(outward)

# function

# def greet_user():
#     print("hi Priyanka")
#     print("Welcome in my world")
#
#
# print("Start")
# greet_user()
# print("finish")

# parameters

# def greet_user(name):
#     print("hii", name,"!")
#     print(f'hi {name}!')
#     print("welcome in my world")
#
#
# print("start")
# greet_user("priya")
# greet_user("shivaji")
# print("finish")
#
# def greet_user(first_name, last_name):
#     print("hii", first_name, last_name,"!")
#     print(f'hi {first_name} {last_name}!')
#     print("welcome in my world")
#
#
# print("start")
# greet_user("priya","Gaikwad")
# greet_user("shivaji", "Gaikwad")
# print("finish")

# Key arguments

# def greet_user(first_name, last_name):
#     print(f'hi {first_name} {last_name}!')
#     print("welcome in my world")
#
#
# print("start")
# greet_user(last_name ="priya",first_name ="Miss")
# greet_user(first_name ="shivaji", last_name ="Gaikwad")
# print("finish")

# Return Arguments

# number= int(input("enter any number: "))
# def square(number):
#     return number * number
# #result = square(number)
# ##print(square(3))

# def square(number):
#     return number * number
# result = square(3)
# print(result)

# Expections

# try:
#     age= int(input("Age:"))
#     print(age)
# except ValueError:
#     print("Invalid Valve")


# try:
#     age= int(input("Age:"))
#     income= 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("age cannot be zero")

#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# classes

# class Point:
#     def move(self):
#         print("move")
#
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.draw()
#
# priya = (1:10)
# s= sum(priya)
# print(s)