# just basics
a=1
b=1
print(a+b)

# operators in python
a=10
b=20
c=a+b
print(c)
print(a*b)
print(c//b)
print(a-b)

# comparision operator
d=10>5
print(d)
c= 10==10
print(c)

# logical operators
m=True and False

# type casting and type function
a=30
print(type(a))
b=31.4
print(type(b))
c="Sush"
print(type(c))
x=float(a)
print(x)
print(type(x))

# input function
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("Sum is ", a+b)

a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
print(a>b)

a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
print("Average of 2 numbers are:",(a+b)/2)

a=int(input("Enter a number 1:"))
print("Square of a number",a, "is:",a*a)

# strings
name="Sushmita"
print(len(name)) # to find the lenth of string
print(name[2:4])
print(name[-4:-1])
print(name[1:])
print(name[:8])

# skipping of the string
word="Sushmita"
print(word[1:8:3])

# another types
print(word[9:])
print(word[:9])
print(word[0:9])

string functions
# to find the length 
str="Sammu"
print(len(str))
print(str.endswith("mmu"))
print(str.endswith("mmua")) #to find the if string ends with specific characters or not
print(str.startswith("sa"))#to find the string is start with specific character or not
print(str.capitalize()) # to make the first word as capital
index=str.find("mmu")
print(index) #to find the index of the word
another="sushmita want "
replace=another.replace("sushmita","ranju")
print(replace) # to replace the original string

# problms
name=input("Ente your name:")
print(f"Good evening {name}")

letter='''
Dear <|name|>,
You are selected!
<|Date|>
'''
print(letter)

replced_string=letter.replace("<|name|>","Sushmita")
replced_string=letter.replace("<|Date|>","28/10/2028")
print(replced_string)
print(letter.replace("<|name|>","Sammu").replace("<|Date|>","28/10/2028")) # if we want to replace in one line of code

name="Sushmita is a good girl"
print(name.find("is"))
print(name.replace(" ","     ")) # strings are immutable

sentence="Dear Sushmita,\n\t you are a quick learner,\nthank you"
print(sentence)

list and tuple
names=["Sammu","ramju","Sussu","Shara","nishmi"]
print(names)
names[1]="Sanika"
print(names)
print(names[0:4]) #slicing of list

# methods of string
names.append("Sanika") # to add the new elem into list
print(names)

numbers=[23,45,12,34,56,76,43,23]
numbers.sort() # to sort the given lost
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(4,100) # inserting the new value at respected index with new value or elem
print(numbers)
numbers.pop(3)
print(numbers)
print(numbers.pop(3))
numbers.remove(56)
print(numbers)
