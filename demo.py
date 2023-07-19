## practice of the python programming

# dna_seq = "AATTGGCCCGATTAGCAGCATAGCATGAC"
# def nuc(dna_seq):
#     n=0
#     AT_count= 0
#     for i in dna_seq:
#         if (i=="A") or (i =="T"):
#             AT_count +=1
#         n+=1
#     AT_per = (AT_count/n)*100
#     print("AT_per in the given sequence is: " , AT_per)
#     return AT_count
# print(nuc(dna_seq))

# l= [1,2,3,4,"priya","shivaji",[7,8,9],"manisha"]
# def test3(l):
#     a=[]
#     for i in l:
#         if type(i)==list:
#             for j in i:
#                 a.append(j)
#         else:
#              if type(i)==int or type(i)== float:
#                     a.append(i)
#     return a
# print(test3(l))

# i = int(input("enter any number: "))
# def square(number):
#     return number*number
# print(square(i))

# def name():
#     print("priyanka")
#     print("shivaji gaikwad")
# name()
# name()
# name()

# def name(a):
#     print(a, "priya")
#     print("pondicherry university")
# name("hello")


### simple calculator by using function with while loop and if else
# def main():
#     print("Welcome to the calculator program!")
#     while True:
#         print("Please select an operation:")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Quit")
#         choice = input("Enter your choice (1-5): ")
#         if choice == "5":
#             print("Thank you for using the calculator program!")
#             break
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         if choice == "1":
#             result = num1+num2
#             print("Result: ", result)
#             break
#         elif choice== "2":
#             result = num1-num2
#             print("Result: ", result)
#             break
#         elif choice == "3":
#             result = num1*num2
#             print("Result: ", result)
#             break
#         elif choice == "4":
#             result = num1/num2
#             print("Result: ", result)
#             break
#         else:
#             print("Invalid choice. Please try again.")
#             break
# # Call the main function
# main()

# Define a function to add two numbers
# def add(num1, num2):
#     return num1 + num2
#
# # Define a function to subtract two numbers
# def subtract(num1, num2):
#     return num1 - num2
#
# # Define a function to multiply two numbers
# def multiply(num1, num2):
#     return num1 * num2
#
# # Define a function to divide two numbers
# def divide(num1, num2):
#     if num2 == 0:
#         return "Error: Cannot divide by zero"
#     else:
#         return num1 / num2
# print(add(5,6))


# print("simple calculator for calcualtion")
# print("select any number for doing the operation")
# print("1. addition")
# print("2. substaction")
# print("3. multiplication")
# print("4 division")
#
# number = int(input("select any operation : "))
#
# if number ==1:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     print("the sum of the two number is: " , str(int(num1+num2)))
# elif number ==2:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     print("the substraction of the two number is: " , str(int(num1-num2)))
# elif number ==3:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     print("the multiplication of the two number is: " , str(int(num1*num2)))
# elif number ==4:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     print("the division of the two number is: " , str(int(num1/num2)))
# else:
#     print("select only the given operation number")

## sum by using for loop

#l=[1,2,3,4,5]
# sum= 0
# for i in l:
#     sum += i
# print(sum)

# l1=[]
# for i in l:
#     l1.append(i*2)
# print(l1)

# name =["priya","shivaji","manisha","gaikwad"]
# name1 =[]
# for i in name:
#     name1.append(i.upper())
# print(name1)

# data =[1,3,"priya",1.2,2.3,"shivaji","manisha",8,"gaikwad"]
# data1 =[]
# data2 =[]
# for i in data:
#     if type(i)==int or type(i)==float:
#         data1.append(i)
#     else:
#         data2.append(i)
# print(data1)
# print(data2)

## else statement with for loop

# l =[1,2,3,4,5]
# for i in l:
#     print(i)
# else:
#     print("priyanka")
#
#
# l =[1,2,3,4,5]
# for i in l:
#     if i==2:
#         break
#     print(i)
# else:
#     print("priyanka")
#
#
# l =[1,2,3,4,5]
# for i in l:
#     if i == 4:
#         continue
#     print(i)
# else:
#     print("priyanka")

# print(range(5))
# print(range(1,5))
# print(list(range(5)))

# name =["priya","shivaji","manisha","gaikwad"]
# print(len(name))
# print(list(range(len(name))))
# print(list(range(len(name)-1,-1,-1)))
#
# for i in list(range(len(name)-1,-1,-1)):
#     print(name[i])
#
# l= [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(l),2):
#     print(l[i])

# name = "priyanka gaikwad"
# for i in name:
#     print(i)

#dic = {"name": "priyanka","sub":"python","reg.no":15,"topic":["introduction","material","methodology","result","reference"]}
# print(dic.keys())
# print(dic.values())
# print(dic.items())


# for i in dic.keys():
#     print(i)
#
# for i in dic.values():
#     print(i)
#
# for i in dic.items():
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(10):
#     print("priyanka",i*'*')

# a = int(input("enter any num: "))
# for i in range(1,11):
#     result =i*a
#     print(result)

###############################################################

#while loop

# a = int (input("enter any num: "))
# start =1
# sum =0
# while a>=start:
#     sum = sum+start
#     start =start+1
# print(sum)


# x= int (input("enter any num: "))
# factorial = 1
# while x>0:
#     factorial =factorial*x
#     x= x-1
# print(factorial)

# x = int(input("enter any num: "))
# a=1
# while a<=10:
#     result = x*a
#     print(result)
#     a+= 1

# a=1
# while a<=5:
#     print(a)
#     a+=1
# else:
#     print("priyanka shivaji gaikwad")
#
# a=1
# while a<=5:
#     print(a)
#     if a== 3:
#         break
#     a+=1
# else:
#     print("priyanka shivaji gaikwad")


## list comprehension

# print([i for i in range(5)])
# print([i**2 for i in [1,5,6,7]])
# print([i.upper() for i in ["priya","shivaji","gaikwad"]])
# print([i+2 for i in range(10)])
# print([i for i in range(10) if i%2==0])
# print([i for i in range(10) if i%2 != 0])

## tuple comprehension

# print(list(i for i in range(10)))
# print(list(i**2 for i in range(5)))
#print(list(i for i in range(10) if i%4==0))

## dictionary comprehension
# d = {1:2,2:3,3:4,4:5}
# print({k:v**2 for k,v in d.items()})
# print({v for k,v in d.items() if v>2})

#######################################################

## function

# def name():
#     print("priyanka shivaji gaikwad")
# print ("hello")
# name()
# print("nice to meet you!!")

# def name2():
#     a = "hii priyanka ,how are you?"
#     return a
# print(name2() + " nice to meet you")

# def test ():
#     return 1,2,"priya",5.3,6+5j
# print(test())

#nums = [2,7,11,15]
# sum=0
# for i in nums:
#     if i<=7:
#         sum = sum+i
# print(sum)

# def sum(nums):
#     a = 0
#     for i in nums:
#         if i<=7:
#           a= a+i
#     return a
# print(sum(nums))

#print(nums[0]+nums[1])


# import json
# data = {"name":"priyanka","fathername":"shivaji", "rollno": 15, "subject": ["maths","biology","genetics"]}
# with open ("data.json",'w') as a:
#   data1 = json.dumps(data)
#   print(data1)
#
# with open ("data.json", 'r') as a:
#     data2 = json.load(a)
#     print(data2)