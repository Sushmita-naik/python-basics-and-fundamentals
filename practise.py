# # just basics
# a=1
# b=1
# print(a+b)

# # operators in python
# a=10
# b=20
# c=a+b
# print(c)
# print(a*b)
# print(c//b)
# print(a-b)

# # comparision operator
# d=10>5
# print(d)
# c= 10==10
# print(c)

# # logical operators
# m=True and False

# # type casting and type function
# a=30
# print(type(a))
# b=31.4
# print(type(b))
# c="Sush"
# print(type(c))
# x=float(a)
# print(x)
# print(type(x))

# # input function
# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# print("Sum is ", a+b)

# a=int(input("Enter a number 1:"))
# b=int(input("Enter a number 2:"))
# print(a>b)

# a=int(input("Enter a number 1:"))
# b=int(input("Enter a number 2:"))
# print("Average of 2 numbers are:",(a+b)/2)

# a=int(input("Enter a number 1:"))
# print("Square of a number",a, "is:",a*a)

# # strings
# name="Sushmita"
# print(len(name)) # to find the lenth of string
# print(name[2:4])
# print(name[-4:-1])
# print(name[1:])
# print(name[:8])

# # skipping of the string
# word="Sushmita"
# print(word[1:8:3])

# # another types
# print(word[9:])
# print(word[:9])
# print(word[0:9])

# # string functions
# # to find the length 
# str="Sammu"
# print(len(str))
# print(str.endswith("mmu"))
# print(str.endswith("mmua")) #to find the if string ends with specific characters or not
# print(str.startswith("sa"))#to find the string is start with specific character or not
# print(str.capitalize()) # to make the first word as capital
# index=str.find("mmu")
# print(index) #to find the index of the word
# another="sushmita want "
# replace=another.replace("sushmita","ranju")
# print(replace) # to replace the original string

# # problms
# name=input("Ente your name:")
# print(f"Good evening {name}")

# letter='''
# Dear <|name|>,
# You are selected!
# <|Date|>
# '''
# print(letter)

# replced_string=letter.replace("<|name|>","Sushmita")
# replced_string=letter.replace("<|Date|>","28/10/2028")
# print(replced_string)
# print(letter.replace("<|name|>","Sammu").replace("<|Date|>","28/10/2028")) # if we want to replace in one line of code

# name="Sushmita is a good girl"
# print(name.find("is"))
# print(name.replace(" ","     ")) # strings are immutable

# sentence="Dear Sushmita,\n\t you are a quick learner,\nthank you"
# print(sentence)

# list and tuple
# names=["Sammu","ranju","Sussu","Shara","nishmi"]
# print(names)
# names[1]="Sanika"
# print(names)
# print(names[0:4]) #slicing of list

# # methods of string
# names.append("Sanika") # to add the new elem into list
# print(names)

# numbers=[23,45,12,34,56,76,43,23]
# numbers.sort() # to sort the given lost
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.insert(4,100) # inserting the new value at respected index with new value or elem
# print(numbers)
# numbers.pop(3)
# print(numbers)
# print(numbers.pop(3))
# numbers.remove(56)
# print(numbers)

# # tuple
# a=(1,2,3,4,5)
# print(type(a))
# # to create an empty tuple
# b=()
# print(type(b))
# c=("sushmita",123,456,"Ranjita","Sammu",23.45)
# print(c)
# print(c.count(456))
# print(c.index("sushmita"))

# some=(1,2,34,56,78,98,56,34,100)
# print(min(some))
# print(max(some))
# print(len(some))
# print(sum(some))
# print(sorted(some))
# print(tuple(reversed(some)))
# print(some.index(98))
# print(some.count(56))

# # some other tuple operations
# # slicing of tuple
# t1=("Sushmita","Ranjita","Sammu","Sanika","Nishmi")
# print(t1[0:4])
# t2=("Sharanya","Sharadvi","Prakrithi","Shobha")
# T=t1+t2 # concatination of tuple
# print(f"a new tuple is {T}")

# # repetation or multiplication of a tuple
# tup1=(112,34,56,7,83,4,5)
# print(tup1 * 2)
# print(tup1 * 3 )

# # to find if the elem is present or not in the tuple then we use membership operation
# tup2=(1010,2,3,45,6,7,8,56,78)
# print(45 in tup2)
# print(100 in tup2)

# # to compare the 2 tuple then we use comparision operation in tuple
# tup3=(101,230,45)
# tup4=(101,230,45)
# tup5=(102,130,56)
# print(tup3==tup4)
# print(tup4==tup5)

# # iteration operator
# tup6=(23,45,67,89,90)
# for i in tup6:
#     print(i)

# # removing and adding the tuples values to anothe variable use packaging and unpackaging (to add the value in unpacking variable)
# t=(19,68,78,90)
# x,y,z,l=t
# print(x,y,z,l)

# # problems
# fruits=[]
# f1=input("Enter one fruit:")
# f2=input("Enter another fruit:")
# f3=input("Enter next fruit:")
# f4=input("Enter next fruit:")
# fruits.append(f1)
# fruits.append(f2)
# fruits.append(f3)
# fruits.append(f4)
# print(f"The final list that has fruits is {fruits}")

# marks=[]
# m1=float(input("Enter first student marks:"))
# m2=float(input("Enter second student marks:"))
# m3=float(input("Enter third student marks:"))
# m4=float(input("Enter fourth student marks:"))
# m5=float(input("Enter fifth student marks:"))
# m6=float(input("Enter sixth student marks:"))
# marks.append(m1)
# marks.append(m2)
# marks.append(m3)
# marks.append(m4)
# marks.append(m5)
# marks.append(m6)
# print(marks)
# marks.sort()
# print(marks)

tuple=("Sushmita","Ranjita","Sammu")
tuple[1]="SSS"

list=[23,45,67,89,98,103]
print(sum(list))

a=(7,0,8,0,0,9)
print(a.count(0))

marks=[78,65,89,45,92]
total=sum(marks)
print("The total marks are:",sum(marks))
print("The highest marks is:",max(marks))
print("The lowest marks is:",min(marks))
length=len(marks)
avg=total/length
print(avg)

# dictionary : used to store the element in key value pairs
table = {
    "name":"Sushmita",
    "sslc_marks": 95,
    "school":"JVMK",
    "university":"AIET",
}
print(table)
print(type(table))
print(table["name"]) # to get the value of the respective key in the dict

# we can store a list in dict also 
dict={
    "name":"Sushmita",
    "marks":[100,99,20]
}
print(dict)
print(dict["name"])
print(dict["marks"])

# dictionary methods
print(dict.items())
print(dict.keys())
print(dict.values())
dict.update({"name":"Ranjita","age":19})
print(dict)
print(dict.get("age2")) # prints none
print(dict["age2"]) #returns an error
dict.pop("age")
print(dict)
dict.popitem()
print(dict)
dict2=dict.copy()
print(dict2)

# sets in python
# can't contain repeating elem
set1={}
set2={1,2,3}
print(type(set1)) # returns the type i.e dict
print(type(set2)) # returns type is set

name=set() # to create an empty set
set={1,2,3,4,5,6,6,7,5,8,9}
print(set)

# set methods
set1={23,45,67,"Sussu","Biri",23,45.6}
set1.add(45.6)
print(set1)
set1.remove("Sussu")
print(set1)
set1.pop()
print(set1)

# union and intersection of sets
set3={12,34,56,65,43,45,78}
set4={4,45,23,78,39,56,12,34}
print("The union of set3 qnd set4 is",set3.union(set4))
print("The intersection of set3 qnd set4 is",set3.intersection(set4))
print(set3-set4)

set5={1,2,3,4}
set6={1,2,3}
print(set6.issubset(set5))
print(set6.issuperset(set5))
print(set5.isdisjoint(set6))

# problems
dict={
    "enu":"What",
    "yaavdu":"which",
    "yaake":"why"
}
mean=input("Enter the word to get the meaning:")
print(dict[mean])