import csv  ## fle handling practice

# file = open("pondy.txt", "w")
# file.write("pondicherry is the very beautiful city, it is my favourite place")
#
# file = open("pondy.txt", "r")
# data = file.read()
# print(data)
#
# file= open("pondy.txt","a")
# data1 = file.write("I am priyanka shivaji gaikwad, I am student of the pondicherry university")
# print(data1)
# file.close()
#
# ## read and write file without close
#
# with open("pondy.txt", "w") as a:
#     a.write("I am good girl")
# with open("pondy.txt", "r") as b:
#     data= b.read()
#     print(data)
# with open("pondy.txt","a") as c:
#     data1 = c.write("I love BTS")
#     print(data1)

##############################################
## json module in file handling in python

# import json
# data = {"name": "priyanka", "subject": "python", "marks": 95, "age":23, "hobby":"coding"}
# with open("pondy.json", "w") as a:
#     json.dump(data, a)
# with open("pondy.json", "r") as b:
#     data1 = json.load(b)
#     print(data1)
#
# # append the new data in existing json file
# # we can not append the data in json file because dictionary do have append attribute
# new_data = {"name": "harshada", "subject": "java","marks": 99, "hobby": "reading"}
# data1.append(new_data)
# with open("pondy.json","w") as d:
#     json.dump(data1, d)


########################################

## handling of cev file with loop
#import csv
# data = [["name", "rollno", "subject","marks"],
#         ["priyanka",15,"maths",95],
#         ["harshada",16,"science",98],
#         ["devansh",14,"marathi", 100],
#         ["manisha", 18, "english",60]]
#
# with open("pondy.csv", "w") as a:
#     data1 = csv.writer(a)
#     for i in data:
#         print(data1.writerow(i))


## handling the csv file without the loop
## use newline function
# import csv
# data = [["name", "rollno", "subject","marks"],
#         ["priyanka",15,"maths",95],
#         ["harshada",16,"science",98],
#         ["devansh",14,"marathi", 100],
#         ["manisha", 18, "english",90],
#         ["shivaji",20, "history", 85]]
#
# with open("pondy.csv", "w", newline = "") as a:
#     data1 = csv.writer(a)
#     data1.writerows(data)
#
# with open("pondy.csv", "r") as b:
#     data2 = csv.reader(b)
#     # for i in data2:
#     #     print(i)
#     for i in data2:
#         print(i[2])


##  read csv file in dictionary format

# with open ("pondy.csv", "r") as c:
#     data3 = csv.DictReader(c)
#     for i in data3:
#         print(i)








