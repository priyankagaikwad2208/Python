#first lecture

#x= 1+1
#print (x)
#print(1+1)

#a= 10
#b= 20
#print(a+b)
#print(type(a))
#print(type(b))

# x= 2.6
# print (x)
# print(type(x))
#
# s = "priyanka"
# print(s)
# print(type(s))
#
# p = "hey, I am priyanka"
# print(p)
#
# a =str(6)
# b="priyanka"
# print(a+ b)
#
# n = True
# print(type(n))
#
# m = False
# print(type (m))
# print(n+m)
# print(True*True)
# print(True * False)
#
#
# v = 4+5j
# print(type(v))
# v = 4+5J
# print(type(v))
# print(v.real)
# print(v.imag)
#
# a = "pwskill"
# print(a[0])
# print(a[-1])
# print(a[0:3])
# print(a[::])
# print(a[0:])
# print(a[:1])
# print(a[0:4])
# print(a[0::2])
# print(a[0:7:2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[1:7:-1])
# print(a[8: :-1])
# print(a[-2:-8:-1])
# #print(a[20])
# print(a[:20])
# print(a[:-20:-1])
#
# name= "priyanka shivaji gaikwad"
# print(len(name))
# print(name.find("a"))
# print(name.find("shivaji"))
#
# print(name.count("a"))
# print(name.count(s ))
# print(name.count("m"))
# print(name.upper())
#
# jk = "PRIYANKA SHIVAJI GAIKWAD "
# print(jk.lower())
# print(jk.title())
# print(jk.capitalize())
# print(jk + " JUNKOOK")
# print(jk + "123")
# print(jk+ str(456))
# print(jk* 3)
# #print(jk/2)

# print("dont't do copy in my class")
# print('don"t do copy in my class')


################################################################################
#practice of first lec
# n=2
# print(n)
# m = 6
# print(n+m)
# a = 4+7j
# print(a.real)
# print(a.imag)
# x = 2.5
# print(x)
# print(type(n))
# print(type(a))
# print(type(x))
# print (int(x))
# print(m*n)
# print(m/n)
# print(m//n)
# print(m%n)

# name = "junkook is my favourite BTS member. "
# print(name)
# print (len(name))
# print(name.upper())
# print(name.lower())
# print(type(name))
# print(name.title())
# print(name.capitalize())
#
# dream = "my dream is to meet the junkook"
# print(dream)
# print(name+dream)
#
# #print(dream + str(x))
# print(name* 5)
# print(name[0::1])
# print(name[::])
# print(name[0:7])
# print(dream[-1])
# print(dream[-1:-8:-1])
# print(name[0::2])
# print(name[24:28])
# print(name[-8::1])
# print(name.count("a"))
# print(name.count("o"))
# bts = name.replace('favourite','bestfriend')
# print(bts)
# print(name.find("kook"))

####################################################################################

#second lecture
##list datatype

# data = [1, 2, 3, 5 + 4j, "radha", "shyam", 9, "shivaji", 4.2, 6, 2.9]
# print(data)
# print(type(data))
# print(data[0:5])
# print(data[7])
# print(data[0:3])
# print(data[-1])
# print(data[::-1])
# print(data[0::2])
# bts = "junkook"
# a =(list(bts))
# print(a)
# print(data + a)
# print(data[5])
# print(type(data[5]))
# print(data[5][0:2])


##############################################################################
# info = [5,"priya",5.4,5+4j, 2, "shivaji",55,2.3]
# print(info)
# print(type(info))
# print(info[0::2])
# print(len(info))
# jk = "junkook"
# print(jk)
# a= (list(jk))
# print(a)
# print(info+a)
# print(info[5])
# print(info[5][0:5])
# print(info[1][3:5])
# #print(info+ 50)   we can only add list +list so that we have to convert int datatype to list
#
# num = [1,2,3,4,5]
# print(num)
# print(info+num)
# print(num*4)
# print(len(num))
#
# ##append function
# info.append("manisha")
# print(info)
# info.append(jk)
# print(info)
# info.append(num)
# print(info)
# print(info[10][2])
#
# ##extend function
# #extend function unrapped the data and then add in the list
# info.extend("harshu")
# print(info)
# # info.extend(10)     int datatype can not be used for extend function
# # print(info)
# info.extend([7,8,9])
# print(info)
#
# ##insert function
# #insert function is used to add the data at desirable index position in the list
# info.insert(2,"jhope")
# print(info)
# info.insert(5,[4,2,6])
# print(info)
# info.insert(-1,45)
# print(info)
# print(info[-1])
#
# ##pop function
# #pop function used for delete the data form list
# info.pop()
# print(info)
# info.pop(2)
# print(info)
# info.pop(3)
# print(info)
#
# ##remove function
# #remove function used for delete the value
#
# info.remove(55)
# print(info)
# info.remove(5.4)
# print(info)
# info[2].remove(6)
# print(info)
# info.append(45)
# print(info)
# info.remove(45)
# print(info)
#
# ##reverse function
#
# print(info[::-1])   # temporary reverse the element in list
# print(info)
# info.reverse()     #permenantly reverse the element in the list
# print(info)
#
# ##sort function
# # info.sort()      for sort function we have to use int datatype , in this example str and int datatype are used
# # print(info)
#
# data = [4,5,3,1,9,6,10,4,2]
# data.sort()
# print(data) #sort the list in the increasing order
#
# name = ["priyanka","shivaji","gaikwad","manisha","junkook","jin"]
# print(name)
# name.sort()
# print(name)  #sort the list in the alphabetically order
# name.sort(reverse=True)
# print(name)  #by using reverse function we can sort list in reverse order
#
# data.sort(reverse=True)
# print(data)  #arrange the the data in the desending order
#
# print(name.index("priyanka"))
# print(name.count("priyanka"))
# string = "priyanka"
# print(string[0])
# # string[0]= "P"
# # print(string)
#
# lis = [1,5,6,8]
# print(lis[0])
# lis[0]= 9
# print(lis)
#
# name[0]= "jimin"
# print(name)
#
# ## replace function
# #replace function is used for replace the world in the string or list
#
# father = "shivaji"
# print(father.replace('s','S'))

###############################################################
#tuples

# data = (1,5,6+5j,"maya",5.3,"aakash",4,"sharad",[9,10,4.2,6+5j])
# print(data)
# print(type(data))
# print(len(data))
# print(data[2])
# print(data[-1])
# print(data[::-1])
# print(data[-1][0])
#
# lis = [1,5,"shivaji",6,"manisha","priya",3,5]
# tup =(1,5,"shivaji",6,"manisha","priya",3,5)
# print(type(lis))
# print(type(tup))
# lis[3]= 50
# print(lis)
# #tup[3]=40     in tuple we cannot replace the element
# #print(tup)
# print(tup[::-1])
# print(tup.count(5))
# print(tup.index("shivaji"))
# print(tup.index("manisha"))
#
# ##set
# s= {1,5,"shivaji",6,"manisha","priya",3,5}
# print(s)
# print(type(s))
# a={}
# print(type(a))
# b= {1,2,3,4,5,6}
# print(type(b))
# x= {1,2,5,6,(6,0,1)}   # in set we can only put the inmutable intity we can add mutable intity , list can not add in the set
# print(x)
# d= {10,20,1,2,3,4,1,2,3,4,5,6,4,1,1,2,2,3,3,4}  # set removes the duplicate values
# print(d)
# p = [10,20,1,2,3,4,1,2,3,4,5,6,4,1,1,2,2,3,3,4]   # when we want to remove the repeated number in the list we can use the set function
# print(set(p))
# print(list(set(p)))
# r= {50,23,15,95,"shivaji","priya",8,60,52}  # set never arrange the data
# print(r)
# #print(r[0])  we can not use the index operation in the set
# #print(r[::2])    we can not use the splicing operation in the set
#
# #add,remove operation
# r.add(99)
# print(r)
# r.remove(23)
# print(r)

##########################################################################################################################

##practice
# list

# bts = ["junkook",5,2.3,1,6+4j,"jimin",4,"jin",7,True,"taehyung",1,"rm","suga","jhope"]
# print(bts)
# print(len(bts))
# print(type(bts))
# print(bts.index("jimin"))
# print(bts.count(1))
# print(bts[0])
# print(bts[0:6])
# print(bts[::-1])
# print(bts[0::2])
# print(bts[-1:-10:-2])
#bpink =["lisa","rose","jenni","jisoo"]
# print(bpink)
# print(bts+bpink)
# print(type(bpink))
# name= "priyanka"
# print(list(name))
# print(bts +list(name))
# bts.append("priyanka")
# print(bts)
# bts.append(55)
# print(bts)
# bpink.extend("harshada")
# print(bpink)
# bpink.extend([1,2,3])
# print(bpink)
# bpink.insert(2,"priyanka")
# bpink.insert(-1,5)
# print(bpink)
# print(bpink)
# bpink.insert(5,20)
# print(bpink)
# bts.remove(2.3)
# print(bts)
# bts.pop()
# print(bts)
# bts.pop(2)
# print(bts)
# bts.reverse()
# print(bts)
# print(bts[::-1])
#
# num=[5,9,3,4,0,6,7,2,1,3]
# print(num)
# num.sort()
# print(num)
# print(num.index(4))
# num.sort(reverse=True)
# print(num)
# print(num.count(3))
# print(num.count(1))
# bts[0]= "shivaji"
# print(bts)
#
# fruit = "mango"
# fruit.replace('m','M')
# print(fruit)


######## tuple

# tup = ("junkook",5,2.3,1,6+4j,"jimin",4,"jin",7,True,"taehyung",1,"rm","suga","jhope")
# print(tup)
# print(type(tup))
# print(len(tup))
# print(tup[0::])
# print(tup[0:6])
# print(tup[::-1])
# print(tup[-1::-2])
# print(tup.count(5))
# print(tup.index("jin"))
#
# x= {}
# print(x)
# print(type(x))
# a= {1,2,5,6,1,2,3,4,5,9,6,1,2,1,1,1,2,3,3,3}
# print(a)
# print(type(a))
# p= list(a)
# print(p)
# q = set(p)
# print(q)
# a.add("priyanka")
# print(a)
# a.remove(9)
# print(a)


################################################################################################

#Third lecture
#dictionary

# dic = {}
# print(type(dic))
# # in dictionry data are store in key and value form
#
# data ={"name":"priyanka", "fathername":"shivaji","rollno":15,"band":"bts","star":"junkook"}
# print(data)
# print(type(data))
#
# d2 ={123:"priya",456:"shivaji",True:12}
# print(d2)
# print(d2[1])  ##internally True is store in the form of 1 , so by using 1 we can access the True value
# print(d2[True])
#
# print(data["name"])
# print(data["band"])
#
# info ={"name":"priyanka", "fathername":"shivaji","rollno":15,"band":"bts","star":"junkook", "name":"manisha"}
# print(info)
# print(info["name"])
#
# study = {"college":"PU","dept":"bioinformatics","year":"first", "sub":["python","datascience,","java","programming"]}
# print(study)
# print(study["sub"])
# print(study["sub"][1])
#
# family = {"name":["priya","shivaji","manisha"], "number":(1,5,6,2,3,4), "hobby":{"roaming","study","cooking"},"day":{"monday":1,"tuesday":2,"sunday":3} }
# print(family)
# print(family["day"])
# print(family["day"]["tuesday"])
# family["teacher"] = ["sayad","kumar","suresh","amutha"]
# print(family)
# family["teacher"]="pan"
# print(family)
# del family["teacher"]
# print(family)
# print(family.keys())
# print(list(family.keys()))
# print(family.values())
# print(list(family.values()))
# print(family.items())
# print(list(family.items()))
# family.pop("day")
#print(family)

############################################################################################

#decision making statement
#if else statement
# marks = int(input("enter your marks"))
# if marks>=90 and marks<100:
#     print("the grade is first class")
# elif marks>=80 and marks<90:
#     print("the grade is second class")
# elif marks>=70 and marks<80:
#     print("the grade is third class")
# else:
#     print("you have to do study")
# print("i am student of pondicherry university")

# price = int(input("enter the price of the fruit: "))
# if price>=100 :
#     print("the price of the fruit is high")
# elif price>=50 and price <100:
#     print("this fruit is affordable")
# else:
#     print("fruit are fresh")
# print("fruits are good for the health. \n""we should have the eat fruit daily")


# price = int(input("enter the price of the pen: "))
# if price>= 500:
#     if price >600:
#         print("pen is very costly")
#     elif price> 510:
#         print("pen is the best")
# elif price <= 200 and price> 100:
#     print ("i want to buy the pen ")

############################################################################################

#for loop

# l= [1,2,3,4,5,6,7,8,9]
# l2=[]
# for num in l:
#     print(num*2)
#     l2.append(num*2)
# print(l2)
#
# name = ["priya","shivaji","gaikwad","manisha"]
# name2=[]
# for i in name:
#     print(i.upper())
#     name2.append(i.upper())
# print(name2)
#
# data = [1,2,3,4,5,"priya","shivaji",6.3,6+5,8,"manisha"]
# data1=[]
# data2=[]
# for i in data:
#     if type(i) == int or type(i)== float:
#         data1.append(i)
#     else:
#         data2.append(i)
# print(data1)
# print(data2)

# data = ["priya","shivaji",1,5.85,2,3,"manisha","harshu",5,6,4.5]
# str_data =[]
# num_data =[]
# for i in data:
#     if type(i) == int or type(i)==float:
#         str_data.append(i)
#     else:
#         num_data.append(i)
# print(str_data)
# print(num_data)

# family= ["shivaji","manisha","baby","priyanka","harshada","soham"]
# family2=[]
# for i in family:
#     family2.append(i.upper())
# print(family2)
######################################################################################

#lecture 4
#for loop

# l =[1,2,5,6,4,3,7,8]
# for i in l:
#     print(i, type(i))
#
# data =["shivaji","manisha","baby","priyanka","harshada","soham"]
# for x in data:
#   print(x)

## for else statement

# l = [1,2,3,4,5]
# for i in l:
#     print(i)
# else:
#     print("I am priyanka shivaji gaikwad, student of pondicherry university.")
#

## break function in for loop
# name=["shivaji","manisha","baby","priyanka","harshada","soham"]
# for i in name:
#     if i=="priyanka":
#         break
#     print(i)
#
# l = [1,2,3,4,5]
# for i in l:
#     print(i)
# else:
#     print("I am priyanka shivaji gaikwad, student of pondicherry university.")
#
# ### else statement is only run when the for loop is completely execute
# ## in this case the for loop is break when i== 2 therefore else statement is not execute
# l = [1,2,3,4,5]
# for i in l:
#     if i == 2:
#         break
#     print(i)
# else:
#     print("I am priyanka shivaji gaikwad, student of pondicherry university.")
#
#
# ##continue function in the for loop
#
# name=["shivaji","manisha","baby","priyanka","harshada","soham"]
# for i in name:
#     if i=="priyanka":
#         continue
#     print(i)
#
# l = [1,2,3,4,5]
# for i in l:
#     if i == 2:
#         continue    ## in continue function the else statement is execute
#     print(i)
# else:
#     print("I am priyanka shivaji gaikwad, student of pondicherry university.")

#### range function

# print(range(5))
# print(list(range(5)))
# print(list(range(0,5)))
# print(list(range(0,5,2)))
# print(list(range(0,20,2)))
# print(list(range(-10,0,2)))

# name=["shivaji","manisha","baby","priyanka","harshada","soham"]
# print(len(name))
# print(list(range(len(name))))
# print(list(range(len(name)-1,-1,-1)))
#
# for i in list(range(5,0,-1)):  ## write the i in name in the reverse order
#     print(name[i])

# for i in range(len(name)-1,-1,-1):  ## we can also write the list in reverse order by using the multiple function
#     print(name[i])

## extract the data from the list at even index by using the for loop
# data2 =[1,2,5,6,4,3,7,8,9,6,3,2,1,4,52]
# print(list(range(0,len(data2),2)))
# for i in range(0,len(data2),2):
#     print(data2[i])


### sum of the element of the list by using for loop

# num=[1,5,6,3,4,8,9,2,7,10]
# sum = 0
# for i in num:
#     sum=sum+i
# print(sum)


## for loop on tuple

# tup=(1,2,3,4,5)
# for i in tup:
#     print(i)
#
# #sum of num in tup
# result=0
# for i in tup:
#     result = result+i
# print(result)
#
# ## for loop on set
#
# s= {1,2,3,4,5,6,7,8,9,10}
# for i in s:
#     print(i)

### string

# name = "shivaji gaikwad"
# for i in name:
#     print(i)

## dictionary

#dic = {"name": "priyanka","sub":"python","reg.no":15,"topic":["introduction","material","methodology","result","reference"]}
# # print(dic)
# # print(dic.keys())
# # print(dic.values())
# print(dic.items())
# #
#for i in dic.keys():
    #print(dic[i])

    #print(i)
#
# for x in dic.values():
#     print(x)
#
# for i in dic.items():
#     print(i)

# for i in range(10):
#     print(i)


# for i in range(1,6):
#     print("Priyanka",i ,i*'*')
#
# for i in range (10):
#     print(i* '*')

## table of number by using the for loop
# a = int (input("enter any num: "))
# for i in range(1,11):
#     result = a*i
#     print(result)

#######################################################################################################

## lecture 5
##while loop

# a = 1
# while a<=10:
#     print(a)
#     a=a+1

## sum of number (input taken from the user)
# a = int(input("enter your number: "))
# start = 1
# sum = 0
# while start<=a:
#     sum = sum+start
#     start = start+1
# print(sum)

## factorial of the given number

# x= int(input("enter your number: "))
# factorial = 1
# while x>0:
#     factorial = factorial*x
#     x = x-1
# print(factorial)


## finonacci series
# num = int (input("enter any number: "))
# a=0
# b=1
# count = 0
# while count<num:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count =count+1

## reverse the word by using the while loop

# name = input("Enter any word: ")
# print(name)
# reverse = ''
# length = len(name)
# while length>0:
#     reverse = reverse + name[length - 1]
#     length = length-1
# print(reverse)

## table of number by using while loop

# x = int(input("Enter the number: "))
# a= 1
# while a<=10:
#     result = a*x
#     print(result)
#     a = a+1

## else with while loop
## when while loop completely execute then else statement also executed
# i = 1
# n= 5
# while i<n:
#     print(i)
#     i = i+1
# else :
#     print("priyanka shivaji gaikwad ")

## break function

# i = 1
# n= 5
# while i<n:
#     print(i)
#     if i==2:
#         break
#     i = i+1
# else :
#     print("priyanka shivaji gaikwad ")
## when while loop is break then else statement is not executed

################################################################################################

#practice of for loop

# l = [1,2,3,4,5,6,7,8,9]
# l2 =[]
# for i in l:
#     l2.append(i*2)
# print(l2)
#
# name = ["priya","shivaji","gaikwad","manisha"]
# name2=[]
# for i in name:
#     name2.append(i.upper())
# print(name2)
#
# data = [1,2,4,"priya",6.3,1,"shivaji"]
# data1=[]
# data2=[]
# for i in data:
#     if type(i)==int or type(i)==float:
#         data1.append(i)
#     else:
#         data2.append(i)
# print(data1)
# print(data2)


######################################################################################################
## lecture 6
## list comprehension

# l= [1,2,3,4,5,6,7,8,9,10]
# ## by using the loop we have to write so long code but by using the comprehension we can perform the same operation in small code
# # l2=[]
# # for i in l:
# #     l2.append(i*2)
# # print(l2)
#
# ###  by using comprehension
# # print([i*2 for i in l])
# print([i for i in l if i % 2 == 0])
#
# l2 = ["priya","shivaji","gaikwad","manisha"]
# print([i.upper() for i in l2])
#
# ## tuple comprehension
#
# t=(1,2,3,4,5,6)
# print(list(i*  2 for i in t)) ## in tuple comprehension we have to make it list

## dictionary comprehension
## squre of the values present in the dictionry
# d= {"key1":1, "key2":2, "key3":3 , "key4":4}
# print({k: v**2 for k,v in d.items()})
# print({k:v for k,v in d.items() if v>1})

###################################################################################

#lecture 7
## function
# syntax for the function
#     def function_name():
#         function body
#     print(function_name())

# def student():
#     print("I am priyanka gaikwad, I am student of the pondicherry university")
# print("Hello,guys....")
# student()
# print("Nice to meet you!!")

#student() + "shivaji"        ## we can concatinate the fuction with othe datatype by usinf print word,
# if we return the function instead of print the we can concatinate the function

# def student():
#     return"I am priyanka gaikwad, I am student of the pondicherry university,"
# print("Hello,guys....")
# print(student() + " pondicherry")
# print("Nice to meet you!!")

# def test():
#     return 1,2.3,"priya",[4,5,6]
# print(test())
# a,b,c,d = test()
# print(a,b,c,d)
# print(a)
# print(b)
# print(c)
# print(d)

# def operation():
#     a = 1*2*3/2
#     return a
# print(operation()*4)

# def test(a,b,c):
#     d = a*b+c
#     return d
# print(test(4,2,5))
#
# def test2(a,b):
#     return a+b
# print(test2(4,5))
# print(test2("priya ", "gaikwad"))
# print(test2([1,2,3],[4,5,6]))

#l= [1,2,3,4,"priya","shivaji",[7,8,9,"shyam"],"manisha"]
#extract the integer data from the list by using the for loop
# l1=[]
# for i in l:
#     if type(i)==int or type(i)==float:
#         l1.append(i)
# print(l1)

# a = [1,2,4,"priya","shivaji",5.4,[8,9,"manisha"]]
# def data(b):
#     num=[]
#     for i in b:
#         if type(i)== list:
#             for j in i:
#                 if type(j)== int or type(j)==float:
#                     num.append(j)
#         else:
#             if type(i)== int or type(i)==float:
#                 num.append(i)
#     return num
# print(data(a))


# l= [1,2,3,4,"priya","shivaji",[7,8,9,"shyam"],"manisha"]
# def test4(a):
#     l=[]
#     for i in a:
#         if type(i)==list:
#             for j in i:
#                 if type(j)==int:
#                     l.append(j)
#         else:
#              if type(i)==int or type(i)== float:
#                     l.append(i)
#     return l
# print(test4(l))


## reverse the name by usin g the function
# name = "priyanka"
# def name1(b):
#     reverse = ''
#     length = len(name)
#     while length>0:
#         reverse = reverse + name[length -1]
#         length = length- 1
#     return reverse
# print(name1(name))

# def name1(name):
#     reverse = ''
#     length = len(name)
#     while length>0:
#         reverse = reverse + name[length -1]
#         length = length- 1
#     return reverse
# print(name1("shivaji"))

## n no.of argument inside the function

# def test5(*manisha):   ## astrick symbol are used for multiple argument
#     return manisha
# print(test5(1,2,4,5,3))
# print(test5(3,5))
# print(test5(8,6,"priya","shivaji",4+5j))
#
# def test6(*arg,a):
#     return arg,a
# print(test6(1,2,3, a="priya"))
#
# def test8(a,b,c=1,d=2):
#     return a,b,c,d
# print(test8(4,5))
# print(test8(4,5,c=22))
#
# def test9(**manisha):    ## double astrick symbol are used for the key and value pair data
#     return manisha
# print(test9())
# print(type(test9()))      # we can also store the data in the dictionary format
# print(test9(name="priya",age=22,sub="bioinformatics"))

# def name(*n):
#     return n
# print(name("priyanka", "shiavji","gaikwad"))
#
# def x(**name):
#     return name
# print(x(a=2,b=5,c=6))

##########################################################################################

## lecture 8
## generator function

# def fib_num(n):
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
# for i in fib_num(10):
#     print(i)
# print(fib_num(10))

# def count_nu(n):
#     count = 1
#     while count<n:
#         yield count
#         count = count+1
# c = count_nu(5)
# for i in c:
#     print(i)
# print(count_nu(5))

##################################################################################################
## lecture 9
## lambda function

# def num(a,b):
#     return a**b
# print(num(4,3))

# a = lambda a,b : a**b
# print(a(2,2))
#
# add =  lambda x,y : x+y
# print(add(4,5))
#
# c_f = lambda p: (9/5)*p+32
# print(c_f(45))
#
# finding_max = lambda x,y : x if x>y else y
# print(finding_max(20,21))
#
# find_len = lambda x : len(x)
# print(find_len('shivajigaikwad'))

# name = lambda x : x.count('a')
# print(name("priyanka"))

# add = lambda x:x+100
# print(add(50))
#
# product=  lambda x,y,z : x+y*z
# print(product(x=5,z=6,y=8))

# add = lambda x,y=2,z=6 : x+y+z
# print(add(20))

# add = lambda *num : sum(num)
# print(add(20,30,1,0))

# function = lambda x,fun : x+ fun(x)
# print(function(20,lambda x : x*x ))

# num= lambda x: (x % 2 and 'odd' or 'even')
# print(num(16))
# print(num(15))

# name = lambda word : word in "priyanka shivaji gaikwad"
# print(name('priyanka'))
# print(name('manisha'))


#### filter function along with the lambda function
# num =[10,20,14,1,3,2,18,60,44]
# greater = list(filter(lambda num: num>20,num))
# print(greater)

# data = [2,5,6,3,10,42,85,60]
# divide = list(filter(lambda data : data%2==0, data))
# print(divide)

# l= [1,23,4,5,6,7,8,52,50,16,40,48]
# l1 = list(filter(lambda x: x % 4==0,l))
# print(l1)
# l2 = list(filter(lambda x: x%2 == 1,l))
# print(l2)
#
# l3 = [1,-2,-3,-4,20,52,21,30]
# l4= list(filter(lambda x: x<0,l3))
# print(l4)

# data =["priyanka","shivaji","gaikwad","ram","shyam","radha","baby"]
# data1 = list(filter(lambda x: len(x)<6 ,data))
# print(data1)


#### map function along with the lambda function

# data =[2,3,4,5,10,6,20,32,12,15]
# x = list(map(lambda a: a*2, data))
# print(x)
#
# data2 = [2,3,4,5,10,6,20,32,12,15]
# cube = list(map(lambda a: a**3, data2))
# print(cube)

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# print(list(map(lambda x,y: x+y, l1,l2)))

## external function
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# def add(x,y):
#     return x+y
# print(list(map(add,l1,l2)))

# name = "priyanka"
# print(list(map(lambda name: name.upper(), name)))

## reduce function

# from functools import reduce
# l = [6,7,8,9,10,2,3,4,5]
# print(reduce(lambda x,y : x+y,l))
# print(reduce(lambda x,y: x*y ,l))
# print(reduce(lambda x,y : x if x>y else y, l))

##################################################################################################
##lecture 10
## oops in python
## class

# class name():
#     def nam(self):
#         a = "priyanka shiavaji gaikwad"
#         return a
# b = name()
# print(b.nam())
#
# c = name()
# print(c.nam())

# class school():
#     def student(self):
#         print("priyanka shiavji gaikwad")
# shivaji= school()
# shivaji.student()
# print(type(shivaji))

## class and constructor

# class school():
#     def __init__(self,name,rollno, marks,mailid):
#         self.name=name
#         self.rollno = rollno
#         self.marks = marks
#         self.mailid = mailid
#     def fy(self):
#         return self.name , self.rollno, self.marks, self.mailid
# priyanka = school("priya",15,95,"gaikwadpriyanka@gmail.com")
# print(priyanka.fy())
#
# devansh = school("dev",1,96,"devgaikwad@gmail.com")
# print(devansh.fy())
#
# print(priyanka.name)
# print(devansh.mailid)

# class school():
#     def __init__(self,name,rollno, marks,mailid):
#         self.name1=name
#         self.rollno1 = rollno
#         self.marks1 = marks
#         self.mailid1 = mailid
#     def fy(self):
#         return self.name1 , self.rollno1, self.marks1, self.mailid1
# priyanka = school("priya",15,95,"gaikwadpriyanka@gmail.com")
# print(priyanka.fy())
# print(priyanka.name1)

# class student():
#     pass
# student1= student()
# student.name="priya"
# student1.marks =95
# print(student1.name)
# print(student1.marks)


# class student():
#     def did_pass(self):
#         if self.marks>=35:
#             return True
#         else:
#             return False
# student1= student()
# student1.marks = 30
# print(student1.marks)
# did_pass_fail = student1.did_pass()
# print(did_pass_fail)
#
# student2 = student()
# student2.marks= 89
# did_pass_fail = student2.did_pass()
# print(did_pass_fail)
#
# student1.name= "raj"
# student2.name= "priya"
# print(student1.name)
# print(student2.name)

# class complex():
#     def __init__(self,real,imag):
#         self.real= real
#         self.imag =imag
# #
#     def addition(self, number):
#         real= self.real +number.real
#         imag = self.imag+ number.imag
#         result = complex(real,imag)
#         return result
# num1 = complex(1,2)
# num2 =complex(3,4)
# result = num1.addition(num2)
# print(result.real)
# print(result.imag)


# class tringle():
#     def __init__(self, side1, side2,side3):
#         self.side1 =side1
#         self.side2=side2
#         self.side3 = side3
#     def perimeter(self):
#         return self.side1+ self.side2+ self.side3
#
# tranguu = tringle(1,2,3)
# print(tranguu.perimeter())

##########################################################################
# lecture 11
#polymorphism

##  in the below example a and b are two different parameters but by changing the value it is change their nature
# like when we input the two number then addition of two number is done , when we input the string then the two string will be concatinated
# #and this nature of the object is called polymorphism

# def data(a,b):
#  return a+b
# print(data(1,2))
# print(data("priyanka"," gaikwad"))
# print(data([1,2,3],[4,5,6]))


# class data_science():
#  def syllabus(self):
#   print("this is the data science class")
#
# class python():
#  def syllabus(self):
#   print("this is the python class")
#
# def data(object):
#  for i in object:
#   i.syllabus()
#
# data_science =data_science()
# python = python()
#
# object = [data_science , python]
# data(object)


# class girl():
#     def name(self):
#         print("my name is priyanka shivaji gaikwad")
#
# class boy():
#     def name(self):
#         print("my name is devansh shivaji gaikwad")
#
# def student(college):
#     for i in college:
#         i.name()
#
# girl =girl()
# boy = boy()
# college = [girl,boy]
# student(college)


# class car():
#     def __init__(self, name,price, year):
#         self.name = name
#         self.price = price
#         self.year = year
#     def data(self):
#         print("priyanka!!")
#
# class boat():
#     def __init__(self, name , price, year):
#         self.name = name
#         self.price = price
#         self.year = year
#     def data(self):
#         print("Devansh!!")
#
# class plane():
#     def __init__(self,name,price,year):
#         self.name =name
#         self.price =price
#         self.year = year
#     def data(self):
#         return self.name, self.price, self.year
#
# car1 = car("swift", 10000, 2000)
# boat1 = boat("tang", 20000, 2001)
# plane1 = plane("indigo", 30000, 2002)
# print(plane1.data())
#
# for i in (car1,boat1):
#     i.data()
#
# print(car1.name)
# print(boat1.price)
# print(plane1.year)

# class school():
#     def __init__(self, name,rollno):
#         self.name =name
#         self.rollno = rollno
#     def cla(self):
#         print("my name is " ,self.name)
#         print("my roll no is " ,self.rollno)
#
# class collage(school):
#     def data(self):
#         print("priyanka shivaji gaikwad")
#
# s1 = school("priyanka",15)
# s1.cla()

# c1 = collage("devansh", 12)
# c1.cla()


# class car():
#     def __init__ (self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def data(self):
#         print("name of the car is: ", self.name)
#         print("color of the car is: ", self.color)
#         print("price of the car is: ", self.price)
#
#     def speed(self):
#         print("speed of the car is 80 ")
#
#
# class vehical(car):
#     def speed(self):
#         print("speed of the vehical is 90 ")
#
# c1 = car("swift", "white", 50000)
# c1.data()
# c1.speed()
#
# v1 = vehical("tvs", "black", 1000)
# v1.data()
# v1.speed()


# class india():
#     def __init__(self, capital, language, type):
#         self.capital =capital
#         self.language = language
#         self.type = type
#
#     def data(self):
#         print("tha capital of the india is :", self.capital)
#         print("the language of the india is: ", self.language)
#         print("the type of the india is: ", self.type)
#
# class USA():
#     def __init__(self, capital, language, type):
#         self.capital = capital
#         self.language = language
#         self.type = type
#
#     def data(self):
#         print("tha capital of the usa is :", self.capital)
#         print("the language of the usa is: ", self.language)
#         print("the type of the usa is: ", self.type)
#
# obj_india =india("delhi","hindi", "India is developing country")
# obj_usa = USA("washington", "english","usa is a developed country")
#
# country = [obj_india , obj_usa]
# for i in country:
#     i.data()

##################################################################################################

## lecture 12
## Encapsulation
# encapsulation is mechanism of wrapping the data and code acting on the data together in single unit.

# class student():
#     def __init__(self, name, age,mailid):
#         self.__name= name
#         self.__age =age
#         self.__mailid = mailid
#
#     def set_age(self, age):
#         self.__age = 0 if age <0 else age
#     def get_age(self):
#         return self.__age
#
# s1 =student("priyanka",22,"gaikwadpriyanka@gmail.com")
# print(s1._student__name)
# s1.set_age(-2)
# print(s1.get_age())
# s1.set_age(20)
# print(s1.get_age())


# class bank_account():
#     def __init__(self,balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance = self.__balance + amount
#
#     def withdaw(self, amount):
#         if self.__balance >=amount:
#             self.__balance = self.__balance - amount
#             return True
#         else:
#             return False
#     def get_balance(self):
#         return self.__balance
#
# priya = bank_account(1000)
# print(priya.get_balance())
#
# priya.deposit(1000)
# print(priya.get_balance())
#
# priya.withdaw(500)
# print(priya.withdaw(500))
# print(priya.get_balance())
#
# print(priya.withdaw(2000))

###############################################################################################
# lecture 13
## Inheritance

# class student():
#     def girl(self):
#         print("manisha shivaji gaikwad")
# class teacher(student):
#     pass
# s1 = teacher()
# s1.girl()

## multilevel inheritance

# in multilevel inheritance we can herited data from one class to second class then from secon class to third class
## so we can access the data of first class in thord class also
#clid class is act like parent class to another child class

# class student():
#     def girl(self):
#         print("priyanka shivaji gaikwad")
#
# class teacher(student):
#     def boy(self):
#         print("komal mam")
#
# class school(teacher):
#     pass
# s1 = teacher()
# s1.girl()
# a1 = school()
# a1.girl()
# a1.boy()
# s1.boy()
# b1 = student()
# b1.girl()

## multiple inheritance

## in multiple inheritance we can inherited the multiple class in the single class,  we can access the multiple class
## in the single class

# class sister():
#     def girl(self):
#         print("priyanka shivaji gaikwad")
# class brother():
#     def boy(self):
#         print("devansh shivaji gaikwad")
# class mother():
#     def lady(self):
#         print("manisha shivaji gaikwad")
# class father(sister,brother,mother):
#     pass
# f1 = father()
# f1.girl()
# f1.boy()
# f1.lady()


## init function in the inheritance

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks= marks
#     def girl(self):
#         return self.name, self.marks
#
# class teacher(student):
#     def boy(self):
#         print("devansh shivaji gaikwad")
#
# t1 = teacher("priyanka", 95)
# print(t1.girl())
# t1.boy()


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks= marks
#     def girl(self):
#         return self.name, self.marks
#
# class teacher(student):
#     def __init__(self, school, name, marks):
#         student.__init__(self, name ,marks)
#         self.school = school
#     def boy(self):
#         return self.name, self.marks, self.school
#
# t1 = teacher("pondicherry university", "priyanka",95)
# print(t1.boy())
# print(t1.girl())
# print(t1.school)
#
# s1 = student("priyanka" ,95)
# print(s1.girl())


## hierarcial inheritance

# class parent1:
#     def grandfa(self):
#         print("sadashiv gaikwad")
#
# class parent2(parent1):
#     def father(self):
#         print("shivaji gaikwad")
#
# class child(parent1):
#     def me(self):
#         print("priyanka gaikwad")
#
# f1 = parent2()
# c1 = child()
# f1.grandfa()
# c1.grandfa()

######################################################################################
## lecture 14
## abstraction

# import abc
#
# class student():
#     @abc.abstractmethod
#     def name(self):
#         pass
#     @abc.abstractmethod
#     def marks(self):
#         pass
#     @abc.abstractmethod
#     def age(self):
#         pass
#
# class teacher(student):
#     def name(self):
#         print("priyanka shivaji gaikwad")
#
#     def marks(self):
#         print(95)
#
#     def age(self):
#         print(22)
#
# class boy(student):
#     def name(self):
#         print("devansh")
#
# t1 = teacher()
# t1.name()
#
# b1 = boy()
# b1.name()


###################################################################################

#lecture 15
## decorator

# def student(func):
#     def teacher():
#         print("hello i am ")
#         func()
#         print("nice to meet you")
#     return teacher
# @student
# def pondy():
#     print("priyanka")
#
# pondy()


###############################################################################################
## lecturre 16
## class method

# class vehicle():
#   cost = 100000000000
#   def __init__(self, price,color,brand):
#     self.price = price
#     self.color = color
#     self.brand = brand
#
#   @classmethod
#   def details(cls, price, color, brand):
#       print(price, color, brand)
#
#   def car(self):
#     print(self.price, self.color, self.brand, vehicle.cost)
#
# ## creating and calling instance method and add in the class variable
# p1 = vehicle(1000, "white","swift")
# p1.car()
#
# # calling a classmethod
# vehicle.details(2000,"red","baleno")


# class student():
#     marks = 95
#     def __init__(self,name):
#         self.name=name
#
#     @classmethod
#     def student1(cls):
#         print("marks of the student: ", cls.marks)
#
#     @classmethod
#     def student3(cls, age):
#         print("my age is: ", age)
#
#     def student2(self):
#         print("name of the student: ", self.name)
#
# ##calling a classmethod
# student.student1()
#
# ## creating and calling the instances method
# s1 = student("priyanka")
# s1.student2()
#
# student.student3(22)


## add external function in the class

# class vehicle():
#   cost = 100000000000
#   def __init__(self, price,color,brand):
#     self.price = price
#     self.color = color
#     self.brand = brand
#
#   @classmethod
#   def details(priya, price, color, brand):
#     return priya(price, color, brand)
#
#   def car(self):
#     print (self.price, self.color, self.brand, vehicle.cost)
#
# def plane(cls,price,name, color):
#     print(price, name,color)
#
# vehicle.plane = classmethod(plane)
#
# p1 = vehicle.plane(4000,"indigo", "white")
# p1


#######################################################################################################
## lecture 17
## static method
##a static method is a method that belongs to a class rather than an instance
# of the class. It is defined within the class using the @staticmethod decorator
# and does not have access to the instance or its attributes.

# class student():
#   def teacher(self,name,rollno, marks):
#     print(name,rollno,marks)
# s1 = student()
# s1.teacher("priyanka", 15,95)
#
# class student():
#   @staticmethod
#   def school(name,marks,rollno):
#     print(name,marks,rollno)
# student.school("priyanka", 95,15)
#
# class family():
#   @staticmethod
#   def member(name, hobby):
#     print("i am ", name, "my hobby is ", hobby)
# family.member("shivaji gaikwad,", "wathing mobile and enjoying the life")


##To call a static method from a class method in Python, you can simply
# invoke the static method using the class name, followed by the method name.

# class family():
#   @staticmethod
#   def static_method():
#     print("this is the static method")
#
#   @classmethod
#   def class_method(cls):
#     print("this is the class method")
#     cls.static_method()
#
# family.class_method()
# #family.static_method()

## class the static method in the static class

# class student():
#     @staticmethod
#     def student1(list_of_name):
#         print(list_of_name)
#
#     @staticmethod
#     def student2(list_of_hobby):
#         student.student1(["priyanka","shivaji","manisha","devansh","harshada","soham"])
#         print(list_of_hobby)
#
#     @classmethod
#     def student3(cls):
#         cls.student2()
#
# student.student1("priyanka")
# student.student2(["study","watching mobile","cooking","sleeping","reading","playing"])
#

#################################################################################################
#lecture 18
## special magic (dunder) function

##print(dir(int))    ## this print all the dunder function with integer
#print(dir(str))       ## this print all the dunder function with string

# a = 100
# print(a+5)
# #by using dunder function
# print(a.__add__(5))


## in the dunder function first new function will be run after that init function will be run
# class student():
#     def __new__(cls):
#         print("this is the python class")
#     def __init__(self):
#         self.name = "priyanka"
#         print("my name is priyanka")
# s1 = student()


## in this ccode wee write init function first but the new fuction is run
# class student():
#     def __init__(self):
#         print("I am priyanka gaikwad")
#     def __new__(cls):
#         print("this is the python class")
# s1 = student()


## __str__ dunder function in the python

# class student():
#     def __init__(self, num):
#         self.num = num
#
#     def __str__(self):
#         return f"hii guys its me!! {self.num}"
#
# s1 = student(15)
# print(s1)


# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"MyClass instance with value: {self.value}"
#
# # Creating an instance of MyClass
# obj = MyClass(10)
#
# # Printing the object
# print(obj)


# class student():
#     def __init__(self):
#         print(256314)
#
#     def __str__(self):
#         print("hii guys its me!!")
# s1 = student()


####################################################################################################

#lecture 19
## property decorator

#property decorator is a built-in function that allows you to define methods
#that are accessed like attributes. It provides a way to define getter, setter,
# and deleter methods for a class attribute, giving you control over its access and modification.

# class numbers:
#     def __init__(self, price, name):
#         self.__price = price
#         self.name = name
#
# p1 = numbers(100,"manisha")
# print(p1.name)
# print(p1.price)  ## we can not access the price arttribute because it is private


## we can access the private attribute by using @property decorator
# class numbers:
#     def __init__(self, price, name):
#         self.__price = price
#         self.name = name
#
#     @property
#     def access_price(self):
#         return self.__price
#
# p1 = numbers(520, "priyanka")
# print(p1.access_price)
# print(p1.name)

## set the value of the price attribute by using decorator

# class numbers:
#     def __init__(self, price, name):
#         self.__price = price   ## private access modifier
#         self.name = name       ## public access modifier
#
#     @property
#     def access_price(self):
#         return self.__price
#
#     @access_price.setter
#     def set_price(self, course_price):
#         if course_price<=520:
#             pass
#         else:
#             self.__price = course_price
#
# p1 = numbers(520, "priyanka")
# print(p1.access_price)
# p1.set_price = 100
# print(p1.access_price)
# p1.set_price = 1000
# print(p1.access_price)

# class circle():
#     def __init__(self,radius):
#         self.__radius = radius
#
#     @property
#     def access_radius(self):
#         return self.__radius
#
#     @access_radius.setter
#     def set_radius(self, radius2):
#         if radius2 <= 0:
#             pass
#         else:
#             self.__radius == radius2
#
# c1 = circle(5)
# print(c1.access_radius)
# c1.set_radius = 10
# print(c1.access_radius)
# c1.set_radius = -1
# print(c1.access_radius)


#####################################################################################

## file handling in python

 ##write and read the file


# f= open("test.txt" , 'w')
# text = f.write("priyanka shivaji gaikwad")
# f = open("test.txt", 'r')
# text = f.read()
# print(text)
# f.close()
# f = open("test.txt" , 'rb')
# text = f.read()
# print(text)
# f.close()
#
# ## read the file without close
#
# with open("test.txt", 'r') as f:
#     print(f.read())


# data = open("data.txt", 'w')
# data.write("I am priyanka shivaji gaikwad, i live in vidani, my father is farmer, my family is very sweet.")
#
# data = open("data.txt" ,'r')
# a =data.read()
# print(a)
#
# data = open("data.txt", 'a')
# b = data.write("i want to do something special for my family ")
# print(b)

# filename = open("pondy.txt",'w')
# filename.write("I am a studnet")
# filename = open("pondy.txt", 'r')
# data= filename.read()
# print(data)
# filename = open("pondy.txt",'a')
# a= filename.write("i like pondicherry")
# print(a)
# filename.close()


## json module in python

# import json
# data = {"name":"priyanka","fathername":"shivaji", "rollno": 15, "subject": ["maths","biology","genetics"]}
#
# with open("data.json",'w') as a:
#   json.dump(data, a)
#
# with open("data.json", 'r') as a:
#     data2 = json.load(a)
#     print(data2)
# a.close()

#
# import csv
# data = [["name", "rollno", "subject","marks"],
#          ["priyanka",15,"maths",95],
#           ["harshada",16,"science",98],
#          ["devansh",14,"marathi", 100]]
# with open("data.csv" ,'w') as a:
#     writer_data = csv.writer(a)
#     for i in data:
#         print(writer_data.writerow(i))

# with open('data.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#
#     csv_writer.writerow(['Name', 'Age', 'Email'])  # Write header row
#     csv_writer.writerow(['John Doe', 25, 'john@example.com'])  # Write data row
#     csv_writer.writerow(['Jane Smith', 30, 'jane@example.com'])  # Write another data row
#
# with open('data.csv', 'r') as file:
#     csv_reader = csv.reader(file, delimiter=';')
#
#     for row in csv_reader:
#         # Process each row with a semicolon (;) delimiter
#         print(row)

# import csv
#
# data = [
#     ['Name', 'Age', 'Country'],
#     ['John', '25', 'USA'],
#     ['Alice', '30', 'Canada'],
#     ['Bob', '35', 'UK']
# ]
#
# with open('priya.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
# file.close()

# import csv
# data =[["name","subject", "marks", "hobby", "age"],
#        ["priya","maths",98,"reading", 23],
#        ["shivaji","science",98,"watching tv",50],
#        ["manisha","history",85,"cooking", 40],
#        ["soham","english", 95,"playing", 6],
#        ["harshada", "marathi", 85, "writting", 25]]
# with open("family.csv", "w", newline= '') as a:
#     data1 = csv.writer(a)
#     data1.writerows(data)
#
# with open("family.csv","r") as b:
#     data2 = csv.reader(b)
#     for i in data2:
#         print(i)
#         print(i[2])

# import csv
#
# # Writing to CSV
# data = [['Name', 'Age', 'Country'],
#         ['John', '25', 'USA'],
#         ['Alice', '30', 'Canada'],
#         ['Bob', '35', 'UK']]
#
# with open("school.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
# # Reading from CSV
# with open('school.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     with open ("new_school.csv", 'w') as new_file:
#         new_writer = csv.writer(new_file, delimiter = '*')
#         for row in reader:
#             new_writer.writerow(row)
#             print(row)


## reading of csv file dictionary format
# import csv
# with open('school.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         # print(i)
#         print(i['Age'])


####

#binary file formation
##binary file in python used to read ad edit the image , audio, video

# with open("shivaji.bin", "wb") as a:
#     a.write(b"\x01\x02\x03")
#
# with open("shivaji.bin", "rb") as b:
#     c = b.read()
#     print(c)


##########################################################################################

## lecture no =
## buffered read and write other file method

# import io
# with open("buffer.txt", "wb") as a:
#     data = io.BufferedWriter(a)
#     data.write(b"BTS member Jungkook was born in Busan, South Korea. He is 24 years old and is the youngest member of BTS. Jungkook "
#            b"attended the School of Performing Arts Seoul which caused him to start high school a year later than others"
#            b" because of his early debut in the music career.")
#
#     data.flush()
#
# with open("buffer.txt", "rb") as b:
#     data1 = io.BufferedReader(b)
#     data2 = data1.read()
#     print(data2)

###################################################################

## lecture no -
## logging debugger in python

#import logging
# logging.basicConfig(filename= "priyanka.log", level = logging.INFO)
# logging.info("priyanka shivaji gaikwad")
# logging.info("I am good girl")
# logging.info("I am so confident")
#
# # level of logging (info, critical, debug, notset, error, warnning)
#
# logging.error("This is the error")
# logging.critical("this is the critical")
# logging.warning("this is the warning")
#
# logging.debug("this is the debug")
#
# ## we can not print the logging.debug in the info file. when we set the logging.INFO
# # then we can only print the logging.error, logging.critical, logging.warning when we set the logging.INFO
#

## when we set the logging.DEBUG the we can print all the logging function

# logging.basicConfig(filename= "shivaji.log", level= logging.DEBUG)
# logging.debug("This is the debug statement")
# logging.info("this is the info statement")
# logging.error("This is the error")
# logging.critical("this is the critical")
# logging.warning("this is the warning")

## record the time and message in the logging file by using the format

# logging.basicConfig(filename= "test1.log", level= logging.DEBUG, format = '%(asctime)s%(message)s')
# logging.debug("This is the debug statement")
# logging.info("this is the info statement")
# logging.error("This is the error")
# logging.critical("this is the critical")
# logging.warning("this is the warning")
# logging.shutdown()

## record the time, name, levelname, message in the logging file by using the format

# logging.basicConfig(filename= "test2.log", level= logging.DEBUG, format = '%(asctime)s %(name)s %(levelname)s %(message)s')
# logging.debug("This is the debug statement")
# logging.info("this is the info statement")
# logging.error("This is the error")
# logging.critical("this is the critical")
# logging.warning("this is the warning")

############################################################################################################

##lecture no
## modules and import statement

##for that open manishaproject and shivajiproject , in that project we import the module and the packages

################################################################################################################

## lecture no
## exception handling

# a =10
# print(a/0)  ## this is give the error because we can not divide the number with the 0 in the python
# print("priyanka shivaji gaikwad")  ## we can not run this code also because error are already present in our code

## exception handling are used to avoid error
## try block are used for the handle the error and exception block are used for execute the code

# try:
#     a= 10
#     print(a/0)
# except Exception as e:
#     print("priyanka shivaji gaikwad")
# a=3
# print(a+10)


## when we found the error in the try block then only the exception block will be run
# otherwise our try block will be run

# try:
#     a=10
#     print(a*2)
# except Exception as e:
#     print("priyanka shivaji gaikwad")

## else block are also prensent in the python if the try block is execute successfully the else block also execuet

# try:
#     a= 20
#     print(a/2)
# except Exception as e:
#     print("priyanka shivaji gaikwad")
# else:
#     print("our try block is executed")
#
#
# # if the except block will be run then else block does not be run
# try:
#     a= 20
#     print(a/0)
# except Exception as e:
#     print("priyanka shivaji gaikwad")
# else:
#     print("our try block is executed")

## finally block are also present in the pyhton

## if try block is executed the finally block aslo executed
## but if error will be occure in the try block then finally is executed but it will show the error
## because only exception block can be handle the error

# try:
#     print(10+5)
# finally:
#     print("i love mathematics")

# try:
#     print(10/0)
# finally:
#     print("error will be occur")


# try:
#     print(10/0)
# except Exception as a:
#     print("I can handle the error")
# finally:
#     print("i don't know i will be execute or not")
#     print("i was executed")

# try:
#     a = int(input("enter any number: "))
#     b = [1,2,3,4,5]
#     print(b[a])
# except Exception as a:
#     print("invalid index")
# finally:
#     print("i will be print always")

###################################################################################
## lecture no-

## custom exception handling

# class Age(Exception):
#     def __init__(self,msg):
#         self.msg = msg
# def Detail_age(age):
#     if age <0:
#         raise Age("enter age is negative ")
#     elif age>200:
#         raise Age ("enter age is very very high")
#     else:
#         print("enter age is valid")
#
# try:
#     age = int(input("enter your age:"))
#     Detail_age(age)
# except Age as e:
#     print(e)

####################################################################################################

## lecture no
##list of general use exception

# try:
#     a= 10/0
# except ZeroDivisionError as a:
#     print(a)
#
# try :
#     int("priyanka")
# except (ValueError , TypeError) as a:
#     print(a)
#
# try :
#     int("priyanka")
# except (ValueError , TypeError) as a:
#     print("this will catch the error")
#
# try:
#     import harshu
# except ImportError as a:
#     print(a)
# print(10/4)
#
# try:
#     d ={"key": "priyanka", "l" : [1,2,3,4]}
#     print(d["key2"])
# except KeyError as a:
#     print(a)
#
# try:
#     "priya".test()
# except AttributeError as a:
#     print(a)
#
# try:
#     l =[1,2,3,4,5]
#     l[6]
# except IndexError as a:
#     print(a)
#
# try:
#     123+"priya"
# except TypeError as a:
#     print(a)
#
# try:
#     with open ("harshu.txt" , "r") as a:
#         a.read()
# except FileNotFoundError as a:
#     print(a)

##################################################################################

## lecture no
## best practice for exception handling

# always use a specific exception
# try:
#     a = 10/0
# except ZeroDivisionError as a:  ## specific exception
#     print(a)
#

# #print always a proper msg
# try:
#     a = 10/0
# except ZeroDivisionError as a:  ## specific exception
#     print("I am trying to handle zerodivision error")  ## proper msg
#
#

# # always try to log your error
# import logging
# logging.basicConfig(filename = "error.log", level = logging.ERROR)
# try:
#     a = 10/0
# except ZeroDivisionError as a:  ## specific exception
#     logging.error("I am trying to handle zerodivision error {}".format(a))  ## proper msg
#

# # always avoid to write multiple exception handling
# ## in this code error is handle with the Zerodivisionerror , so only write only that exception
# ## don't write other exceptions

# import logging
# logging.basicConfig(filename = "error.log", level = logging.ERROR)
# try:
#     a = 10/0
# except ZeroDivisionError as a:  ## specific exception
#     logging.error("I am trying to handle zerodivision error {}".format(a))  ## proper msg
# except FileNotFoundError as a:  ## specific exception
#     logging.error("I am trying to handle FileNotFoundError {}".format(a))  ## proper msg
# except AttributeError as a:  ## specific exception
#     logging.error("I am trying to handle AttributeError {}".format(a))  ## proper msg

#############################################################################################################

#Lecture no
## multitreading in python

import threading

# def test(id):
#     print("program start %d" , id)
# test(45)

# def test(id):
#     print("program start %d" %id)
# test(45)
#
# thread =[threading.Thread(target = test, args = (i,) )for i in range(10)]
# for t in thread:
#     t.start()

import urllib.request
def file_download()
file_download("https://docs.google.com/document/d/1jUyl6BMyjyZuH9yphFReYtgphi7UFQie/edit")
https://docs.google.com/document/d/1jUyl6BMyjyZuH9yphFReYtgphi7UFQie/edit?usp=sharing&ouid=112237728584804007597&rtpof=true&sd=true