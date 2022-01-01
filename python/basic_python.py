#!/usr/bin/env python
# coding: utf-8

# # **Hello, World!**
# Welcome to the world of python. In this section, we simply print a string using python code. You can say it's kind of a ritual/tradition for anyone who sets on a journey in coding with any language - our way of saying "Hey world, here I come!" 😉  

# In[1]:


print('Hello World!!')
print('Get ready to rock-N-roll ')


# In[2]:


# we saw that the lines automatically shifted to new lines.
# although we can do this manually too, in one print statement

print('Hello World!! \nGet ready to rock-N-roll')


# So what was that `\n` ?
# 
# Read this - https://qr.ae/pGSFo0

# # **Interact with python - get an input/data**
# To do some work, we need something to begin with - right? 
# For example, you need a bat and a ball to play cricket. 
# Similarly, while coding we need some data or input from the user on which we will do some work. 

# In[3]:


#asking user for a text (name)
username = input('Please enter your name - ')

#lets greet the user now
print ('Hello ' +username)


# In[4]:


#OK so lets go one step ahead ;) -- just to give you a feel of what we can do with programming
#now its time to help the user know his/her age

#ask the user's birth year
year = input('Please enter your Birth Year - ')


# In[5]:


#calculating the age, here we have to change the type for year from string to integer
age = 2021-int(year)

#now we will print the results
print(f'Hey {username}, You are {age} year(s) old :) ')


# 
# * using `f` before writing the print statement saves us a lot of time and effort
# * just need to keep in mind that we are keeping the variables in `{}`
# * read more here - https://docs.python.org/3/tutorial/inputoutput.html

# # **Dealing with Numbers**
# So, in programming you can do lots of mathematical operations. But for that you need to have an idea of what are the various datatypes that are to be considered - or even not considered! This section will introduce with some of the possibilities and we'll cover the other complex stuff as we progress.
# 
# You've got it. Keep going! 🙂  

# In[6]:


# first let us understand the datatypes.

# integer datatype
print(f"The datatype for variable 20 is {type(20)}") # <class 'int'>


# In[7]:


# float datatype
print(f"The datatype for variable 20.02 is {type(20.02)}") # <class 'float'>


# In[8]:


# string datatype
print(f"The datatype for variable 'abcd efg hijk lmnop' is {type('abcd efg hijk lmnop')}") #<class 'str'>


# In[9]:


#get the binary for the number
print(bin(2020)) #prints the binary form of 2020 which is 0b11111100100
#get number(integer) from binary form
print(int('0b11111100100', 2)) # 2 for printing the integer form by base as 2

# ---------------- that would be enogh for now to understand about the datatypes.


# In[10]:


# Let us now perform some arithmetic operations

#arithmetic operations without variables
print(f"Sum of 3 and 5 is {3+5}")
print(f"difference of 3 and 5 is {3-5}")
print(f"Product of 3 and 5 is {3*5}")
print(f"Fraction or Division of 3 and 5 is {3/5}")
print(f"exponent of 3 with 5 is {3**5}") #exponent
print(f"Modulus of 3 and 5 is {3%5}")#mod


# In[12]:


#arithmetic operations with variables

a = input("Enter a number. It will be stored as 'a' = ")
b = input("Enter another number. It will be stored as 'b' = ")
#python accepts inputs as str. So whenever we need to perform any mathematical operations, we need to change the datatypes


# In[13]:


print(f"You see, I am writing here a+b but the output will not be the sum. \nInstead, you will see the two numbers will be concatenated! \nHere is the output = {a+b}")


# In[14]:


a = float(a) #keeping in float is safer as user might feed data with decimals
b = float(b) #keeping in float is safer as user might feed data with decimals

print(f"Sum of {a} and {b} is {a+b}")
print(f"difference of {a} and {b} is {a-b}")
print(f"Product of {a} and {b} is {a*b}")
print(f"Fraction or Division of {a} and {b} is {a/b}")
print(f"exponent of {a} with {b} is {a**b}") #exponent
print(f"Modulus of {a} and {b} is {a%b}")#mod


# # **Math Functions in Python**
# To make our lives easier, there are many in-built special functions that are very useful to do specific tasks.
# Here we will see few of the in-built functions that can be used to perform mathematical operations.
# 
# - first we need to import the math module. Read more here https://docs.python.org/3/library/math.html
# - This module provides access to the mathematical functions defined by the C standard.
# 
# - These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place.
# 
# - The following functions are provided by this module. Except when explicitly noted otherwise, all return values are floats.

# In[15]:


#importing the module
import  math


# In[16]:


# --------------Number-theoretic and representation functions--------------------------------------
long_string = '''
math.ceil(x)
Return the ceiling of x, the smallest integer greater than or equal to x.
If x is not a float, delegates to x.__ceil__(), which should return an Integral value.
'''
print(long_string)


# In[17]:


print("\n--------------------math.ceil(x)-------------------------------")
print(f"math.ceil(x) --- for number = 404 --- {math.ceil(404)}")
print(f"math.ceil(x) --- for number = 404.01 --- {math.ceil(404.01)}")
print(f"math.ceil(x) --- for number = 404.36 --- {math.ceil(404.36)}")
print(f"math.ceil(x) --- for number = 404.50 --- {math.ceil(404.50)}")
print(f"math.ceil(x) --- for number = 404.86 --- {math.ceil(404.86)}")
print("---------------------------------------------------------------\n")


# In[18]:


long_string = '''
math.comb(n, k)
Return the number of ways to choose k items from n items without repetition and without order.
Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
Also called the binomial coefficient because it is equivalent to the coefficient of k-th term in polynomial expansion of the expression (1 + x) ** n.
Raises TypeError if either of the arguments are not integers. Raises ValueError if either of the arguments are negative.
'''
print(long_string)


# Explore more here - https://www.programiz.com/python-programming/modules/math
# 
# # **Strings in Python**
# Here we will see how to handle strings in python.
# When we deal with data, we mostly deal with strings - which we then reformat according to our choices.
# So, it is important that we deal properly with the strings such that we don't loose data

# In[19]:


# write a long string (multiple lines without using \n)
long_string = '''
Hello there!
We are currently creating a long string.
Write multiple lines here,
without any worries. B-)
'''
print(long_string)


# In[20]:


#using escape sequences

    #it's difficult to insert a special character in a string or print statement.
    #so, we use \ as our saviour!
print("See, we are writing \" in  a print statement without any worries!")
print('Isn\'t it awesome??')


# In[21]:


#newline
print("This is the first line \nThis is the second line")


# In[22]:


#backspace
print("This is an incomplete li\bne")


# In[23]:


#horizontal tab
print("Here comes the tab\tGot that??")


# In[24]:


#print a backslash itself
print("So, here is the \\ you wanted to see!")


# In[25]:


#formating a string (we have already seen this before, now it is time to realize it !!)
a = 2020
print("This code was written in the year "+str(a)) #here the number is printed in form of a string otherwise it throws an error
                                                    #TypeError: can only concatenate str (not "int") to str
print("After 10 years it will be the year "+str(a+10)) #same explanation as above
#now let us use a shortcut
print(f"The code is written in the year {a}") #see, how simple it is to format a string!!
print(f"After 10 years it will be the year {a+10}")


# In[26]:


#how to get a string index
text = "Climate change is real!"
print(text)
print(text[1:10]) #counting starts from 0
print(text[0:10]) #now see the difference
print(text[:10]) #prints first 10 elements
print(text[::]) #prints Everything
print(text[-1]) #first element starting from the end of the string
print(text[-3]) #third element starting from the end of the string
print(text[::-1]) #prints in reverse order


# * There are many more things to know about strings. 
# * You are welcome to add anything relevant you wish to in this notebook!
# * Please collaborate and contribute :)
# 
# # **String functions in Python**
# Just like we used the math-functions above, this is also quite similar. But here you wouldn't have to import a module.
# Follow the code below (let the code do the talking!)
# Note: This section discusses one of the functions to get you started. There are many more available. Just Google them!
# 
# Reference - https://www.w3schools.com/python/python_ref_string.asp

# In[27]:


mystring = 'lights WILL guide YOU home\n'

# capitalize()	Converts the first character to upper case
print(f"\ncapitalize() Converts the first character to upper case \n\nOriginal string = {mystring} \nResult string = {mystring.capitalize()}")


# In[28]:


# casefold()	Converts string into lower case
print(f"\ncasefold() Converts string into lower case\n\nOriginal string = {mystring} \nResult string = {mystring.casefold()}")


# In[29]:


# center()	Returns a centered string
temp = "banana"
print(f"\ncenter() Returns a centered string\n\nOriginal string = {temp} ")


# In[30]:


temp = temp.center(20, "0")
print(f"\nResult string = {temp}")


# # **Lists in Python**
# Python has several features which are used in all sorts of programming endeavors. One of them is a "list".
# Like always,  Follow the code below (let the code do the talking!)
# 
# This set of codes has been generously contributed by **Mr. Bittesh Barman.**
# 
# Mr. Bittesh is a **PhD student at the Department of Chemistry, Pondicherry University, India**.  <br>
# Visit this URL to view his works - https://www.researchgate.net/profile/Bittesh-Barman-2  <br>
# Thank you!

# In[31]:


# Working with Lists!

cars = ["honda","hundai","tata"] # this is a list type data structure. each elements in list is called item. 
print(cars)
print(cars[0])# we can call any item in this list by its index no.
print(cars[2])


# In[32]:


# Changing items in a list

shoping_cart = ["Pencil", "notebook","book"]
print(shoping_cart)
shoping_cart[0] = "pen" # we can change item by using the index no.
print(shoping_cart)


# In[33]:


#Appending to a list

fruits = ['banana','orange','watermelon']
fruits.append('grapes') # we can add items in list using append method. 
print(fruits)


# In[34]:


# The 'insert()' method!

weapons = ['pan', 'assult rifle', 'shotgun', 'pistol']
weapons.insert(3, 'sniper') # we can add item in any position of  the list by using insert method.
print(weapons)


# # **Tuples in Python**
# A tuple is a sequence of immutable (meaning unchanging over time or unable to be changed) Python objects. 
# Follow the code below (let the code do the talking!)

# In[35]:


#defining a tuple
tuple_1 = ('India', 'Japan', 100, 90, 85674);
tuple_1


# Please note that in defining a tuple, a semicolon is used! (not mandatory though). <br>
# So those python memes donot hold TRUE here 😉

# In[36]:


#size of the tuple
len(tuple_1)


# The size is 5 but if we see the index, it starts with 0. <br>
# Let's have a look here
# 
# 

# In[37]:


#Accessing elements inside the tuple
print(f"The first element - {tuple_1[0]}\nThe second element - {tuple_1[1]}\nThe last element - {tuple_1[len(tuple_1)-1]} ")


# The last element was obtained by using the last index via the code `tuple_1[len(tuple_1)-1]` <br>
# Just for fun!
# 
# **CAUTION - Tuples are immutable**
# 
# So, if we write `tuple_1[0] = some value` we will get an error!

# # **Dictionaries in Python**
# Dictionaries store elements in a key-value pair format. Dictionary elements are accessed via keys while List elements are accessed by their index. 
# Follow the code below (let the code do the talking!)

# In[38]:


#definig a dictionary
dy = { "Country": "India",
         "Currency": "INR",
         "Continent": "Asia",
            "Language": "Multiple"}
dy


# In[39]:


#Access a dictionary (using the key and not the value)
dy["Country"]


# Try this - `dy["India"]`  <br>
# You will get an error. We need to use the key to access a specific value!

# In[40]:


#adding data to dictionary
dy["Capital"] = "Delhi"
dy


# In[41]:


# We can Overwrite dictionary values too

dy["Currency"] = "Indian Rupee"
dy


# In[42]:


# Deleting data in dictionary

del dy["Language"]
dy


# So the Currency key was deleted. <br>
# Now let us delete the whole dictionary

# In[43]:


del dy
#done


# # **Comparison Operators**
# Used to compare 2 or more values and decide if the condition is True or False <br>
# Follow the code below (let the code do the talking!)
# 
# Let us consider a random variable 'x' with a random numerical value stored in it. <br>
# Following is how we can compare the value stored in 'x' with other numerical entities.
# 
# - Equals: x == 5
# - Not equal: x != 5
# - Greater than: x > 5
# - Greater than or equal: x >= 5
# - Less than: x < 5
# - Less than or equal: to x <= 5
# 
# The outcome is always in the form of "True" or "False" - Boolean

# In[44]:


# let us declare a variable with a numerical value
x = 1001

print(x==5)


# In[45]:


print(x!=5)


# In[46]:


print(x > 5)


# In[47]:


print(x >= 5)


# In[48]:


print( x < 5)


# In[49]:


print( x <= 5)


# Now that we know how these work, we can proceed to use them for decision making.
# ie, **If-else statements**
# 
# # **Conditional Statements (IF-ELSE)**
# Think of this scenario - if I score at least 40% in the exam, I will pass, else I will fail.<br>
# So, here the condition for me passing the exam is to reach the 40% mark which can be expressed as ">=" (didn't understand? Study the previous section!) . <br>Now, it just has to be conveyed to the computer and here's how it is done!<br>
# Follow the code below (let the code do the talking!)
# 
# - It is basically the If - else statement
# - If statement is generally followed by an optional else statement
# - The results are always in Boolean
# - else statement works if the if statement returns a FALSE expression.

# In[50]:


pass_marks = float(input("Enter your marks"))
if pass_marks>=40.0:
    print("You passed the exam.")
else:
    print("Well, it didn't work this time. But you can do it. Please don't give up.")


# In[51]:


pass_marks = float(input("Enter your marks"))
if pass_marks>=40.0:
    print("You passed the exam.")
else:
    print("Well, it didn't work this time. But you can do it. Please don't give up.")


# So, that's how we deal with the if-else statements in python.<br>
# Note: **Always remember to take care of the indentation!**
# 
# # **Nested or Multiple IF-ELSE (also called ELIF)??**
# Sometimes, we need to put up multiple conditions for an event to happen. For that, we use IF-ELSE statements multiple times.<br>
# So, this is how we do it in python!
# 
# 
# **Multiple if-else**
# <br>Let us consider that the criteria to get a job interview is atleast 8.0 <br>CGPA and at least 2 years of experience.<br>
# So following would be the way to deal with the situation
# 
# *Note - I'm sad that individuals get judged like this. Skills matter. Not numbers.*

# In[52]:


cgpa = float(input("what is your CGPA out of 10.0?"))
if cgpa >=8.0:
    experience = float(input("how many years of experience do you have?"))
    if experience>=2.0:
        print("You are eligible for an interview")
    else:
        print("Sorry, although you have at least 8.0 GPA, you lack a minimum experience of 2 years.")
else:
    print("Sorry, you need minimum 8.0 CGPA to be eligible")


# In[53]:


cgpa = float(input("what is your CGPA out of 10.0?"))
if cgpa >=8.0:
    experience = float(input("how many years of experience do you have?"))
    if experience>=2.0:
        print("You are eligible for an interview")
    else:
        print("Sorry, although you have at least 8.0 GPA, you lack a minimum experience of 2 years.")
else:
    print("Sorry, you need minimum 8.0 CGPA to be eligible")


# In[54]:


cgpa = float(input("what is your CGPA out of 10.0?"))
if cgpa >=8.0:
    experience = float(input("how many years of experience do you have?"))
    if experience>=2.0:
        print("You are eligible for an interview")
    else:
        print("Sorry, although you have at least 8.0 GPA, you lack a minimum experience of 2 years.")
else:
    print("Sorry, you need minimum 8.0 CGPA to be eligible")


# **The elif statement**
# 
# Let us just write a simple code where the user enters a number from 1 to 5 and the code prints the number in words.
# 
# 

# In[55]:


num = int(input("Enter a number between 1 to 5 - "))
if num == 1:
    print('One')
elif num == 2:
    print('Two')
elif num==3:
    print('Three')
elif num==4:
    print("Four")
else:
    print("Five")


# In[56]:


num = int(input("Enter a number between 1 to 5 - "))
if num == 1:
    print('One')
elif num == 2:
    print('Two')
elif num==3:
    print('Three')
elif num==4:
    print("Four")
else:
    print("Five")


# ...and  we can keep going like this.<br>
# **So, basically the elif statement is nothing but an if statement after an else statement.**

# # **Loops in python**
# 
# Generally, in a program, statements are executed line by line, it means sequentially, but when a block of code needs to be executed multiple times, then what to do? Programming languages comes with that provision also, using loops.
# 
# Python supports two types of loop
# 
# * while loop
# * for loop
# 
# This set of codes has been generously contributed by **Mr. Tapas Saha**. <br>
# Mr. Tapas is a **PhD student at the Department of Computer Science & Engineering, Tezpur University, India**.<br>
#  Visit this URL to view his works - https://www.researchgate.net/profile/Tapas-Saha-3 
# <br>Thank you!
# 
# 
# **While Loop** <br>
# While loop allows the user, to execute a group of statements repeatedly, but it checks the condition before entering the loop body.<br>The repetitions will continue until the condition false.
# 
# Syntax of while loop:
# 
# 
# 
# ```
# while expression:
#   statement(s)
# ```
# 
# 
# 
# Examples:
# 
# - Print the number 1 to 5:

# In[57]:


# initialization 
i=1
while i<=5:
 print("Number ::",i)  # print the sum
 i=i+1


# Another Example
# 
# * Sum of n natural number

# In[58]:


# sum = 1+2+3+...+n

#Take input from the user
n = int(input("Enter n: "))
# initialization 
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    
# print the sum
print("The sum is", sum)


# **For Loops:** <br>
# A for loop is used in python, to execute iterating over the item any sequence.<br>It can be a list, or a tuple, or a dictionary, or a set, or a string.
# 
# Syntax of for loop:
# ```
# for x in sequence :
#   body
# ```
# Example:
# 
# * Print each characters of the given string

# In[59]:


string=" Python"
for i in string :
  print(i)


# Another Example:
# 
# * Print user input string’s each character and index of the characters.

# In[60]:


#Take input from the user,
string=input("Enter some String: ")
# initialization 
i=0 
for x in string :
 print("index of",x,"is:",i) # print
 i=i+1


# One more example!
# 
# * Program to calculate the sum and of all numbers stored in a list

# In[61]:


# List of numbers
n = [4, 9, 5, 10]
# initialization  
sum = 0
mul=1
for i in n:
	sum = sum+i
	mul=mul*i

print("The sum is", sum) #pint
print("The multiplication is", mul)


# # **Functions in python**
# Nothing to write here. Let the code do the talking! 🔥🔥 <br>
# Functions are like recipies. Suppose you and I want to bake a cake. You went online and googled a recipie. Now we both will follow the same recipies but you want to use chololate flavour and I want to use pineapple! So we follow the same recipie but produce new results.
# 
# A function is thus a block of code that can be re-used or run whenever it is needed. Information passed to a function is called an argument (the ingredients for the recipie-analogy)<br>
# 
# **Defining the function** <br>
# Let us create a dedicated function that can add 2 numbers
# 
# 
# 
# 

# In[62]:


#defining the function
def add(a,b):
 return (a+b)


# In[63]:


# Calling a function
# We will now feed some data to the function to get the sum value

x = float(input("Hey user, enter the first number - "))
y = float(input("Nice! now enter the second number - "))
print(f"The sum of {x} and {y} is {add(x,y)}")


# Saw that? Now just imagine how cool it would be to have a dedicated function for doing a more complex task!!
# 
# **Lambda Expressions**
# 
# Lambda function is used to create small elegant anonymous functions, generally used with `filter()` and `map()`

# In[64]:


m = lambda n:n**2
m(3)


# **The `map()` function**
# 
# - This takes in a function and a list.
# - The function perform an operation on the entire list and return the results in a new list.
# - Let us see it work with a simple cube of a number

# In[65]:


my_list = [5, 10, 55 , 568, 468, 77]
output_list = list(map( lambda x: x**3, my_list))
print(output_list)


# **The `filter()` function**
# 
# * This performs an operation on a list based on a specific condition after filtering
# * Let us see it work with a simple condition statement - numbers less than or equal to 201

# In[66]:


my_list = [5, 10, 55 , 568, 468, 77]
condition = list(filter(lambda x: (x <= 201), my_list))
print(condition)


# # **Error handling in python**
# 
# This is one of the most important concepts to make a coder's life easier. 
# Just walk through the code and you'll get what I mean. Let the code do the talking! 🔥🔥 <br>
# 
# While running an automated code that works on unknown or new data, it might happen that the code encounters an error at some point. You, as a coder might not like the execution process to stop. Rather you would like to have a notification that the error was found and that particular execution was bye-passed.
# 
# This is where the **`try-except`** feature of pythons comes to the rescue!

# In[67]:


# understanding an error - let us try to print an undefined variable
print(name)
a=111
b=222
print(a+b)


# In[68]:


# Notice that the consequent codes were not executed after the error.
# Now let us attempt to bye-pass the error part of the code and move on to the next executions

try:
    print(name)
except NameError:
    print("Error - The variable has no value defined to be printed in the first place.")
except:
    print("Error - Not sure what the error is, but there is something wrong!")
a=111
b=222
print(a+b)


# The above example only shows an application of the Built-in exceptions in python.<br>
# There are many Built in Exceptions available to be used.<br>
# You can learn about them here - https://docs.python.org/3/library/exceptions.html#bltin-exceptions <br>
# Till then, have fun!

# # **File handling in python**
# Let the code do the talking! 🔥🔥 <br>
# 
# **File Operations using python**
# * Modes for file handling
# * Creating a file - "x"
# * Reading a file - "r"
# * Writing a file - "w"
# * Appending a file - "a"
# 
# **Creating a file** <br>
# Here we create a .txt (text) file, which we will use in the next steps!

# In[69]:


f = open("file.txt", "x") # open() is used to open the file we want to create/read/write/append


# "f" above can be considered as a file handler. One can use other names too! <br>
# 
# Now it's time to write some data in the file

# In[70]:


f.write("This is a text file!")


# The output above is the number of characters we wrote into the file.
# 
# **Reading a file** <br>
# This only works when the file name mentioned actually exists, just like one can only read a book if the book actually exists!

# In[71]:


f = open("file.txt", "r")
print(f.read())


# **Writing to a file** <br>
# This creates a new file if the file name used does not exist, just like one can write a book if the book does not already exist (I know the analogy is a bit lame, but please bear with me! 😅)

# In[72]:


f = open("file.txt", "w")
f.write("This sentence replaces the sentence already present in the file named 'file.txt'")


# In[73]:


#lets check the result
f = open("file.txt", "r")
print(f.read())


# In[74]:


# Now, let's try writing to a file that does not exist. We will see that the file is created for us before writing into it.

f = open("another-file.txt", "w")
f.write("This sentence is present in the file named 'another-file.txt'")


# In[75]:


f = open("another-file.txt", "r")
print(f.read())


# Nice!!
# 
# **Appendig to a file** <br>
# Works same as writing to a file. Only difference is that it does not replace the pre-existing text.

# In[76]:


f = open("file.txt", "r")
print(f.read())


# In[77]:


f = open("file.txt", "a")
f.write("This sentence appends to the sentence already present in the file named 'file.txt'")


# In[78]:


f = open("file.txt", "r")
print(f.read())


# In[79]:


# Now, let's try appending to a file that does not exist. We will see that the file is created for us before appending into it.

f = open("another-file2.txt", "a")
f.write("This sentence is present in the file named 'another-file2.txt'")


# In[80]:


f = open("another-file2.txt", "r")
print(f.read())


# **Now, that's how we deal with files using python. We can also make files of other extensions like .csv, .tsv, etc in the same procedure!**
