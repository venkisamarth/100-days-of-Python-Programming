# -*- coding: utf-8 -*-
"""day14 condiational statments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JUG_BzDTtT0IxYtjDI0YC8TyoFpek6-k

if statment

the if statement is used for conditional execution of code. It allows you to execute a block of code only if a certain condition is true. Here are five examples to illustrate the use of the if statement in Python:
"""

# Basic if statment
x=100
if x>5:
  print("x is greater thean 5")

"""if-else statment"""

y=3

if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

"""if-elif-statment"""

grade=75
if grade>=90:
  print("A")
elif grade >=80:
  print("B")
elif grade>=70:
  print("C")
else:
  print("Fail")

"""nested if statments

"""

num=15
if num>10:
  if num % 2 ==0:
    print("num is greater than 10 and even")
  else:
    print("numer is greater than 10 but not odd")
else:
    print("number is greater than 10")

"""Ternary Operater

"""

age =25
message="You are young" if age < 30 else "You are not so young anymore"
print(message)

# checking if a number is positive ir negative
num=float(input("Enter  the number "))
if num>=0:
  print("The number is positive.")
else:
  print("The number is negative.")

# Determining if a number is even or odd
num=7
if num%2 == 0:
   print("The numbe even.")
else:
  print("The number is odd.")

# check if a user has access
user_role="admin"
if user_role=="admin":
  print("You have access to all features.")
else:
  print("You have limitd access.")

#chosing the maximum of two numbers
a=15
b=20
if a>b:
  print("The maximum is:",a)
else:
  print("the maximum is:", b)

# checking eligibility  for voting
age=int(input("Enter your age"))
if age>18:
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote yet.")

"""nested if statment"""

# checking the both condiation in a nested manner
x=10
y=5
if x> 5 :
  print("x is greater  than 5")
  if y> 2 :
    print("y is greater than 2.")
  else:
    print("Num is odd")

# nested conditions to check for multiple  cases
num=25
if num>10:
  print("Num is greter than 10.")
  if num %2 ==0:
     print("Num is even.")
  else:
    print("num is odd")

else:
   print("Num is not greate than 10.")

"""Checking  conditions for a password"""

username="user1"
password="pass123"
if username=="user1":
  print("username is correct.")
  if password=="pass123":
    print("pssword is correct .  Login successful")
  else:
     print("Incorrect password. Login faild.")
else:
  print("Incorrect username Login failed.")

#nested if else statment for multiple scrnarios
a=10
b=15
if  a>b:
  print("a is greater than b.")
elif a<b:
  print(" a is less than b")
else:
  print("a is equal to b")
  if a % 2 ==0:
     print(" a is even.")
  else:
    print("a is odd.")

# checking conditions for a shape
shape ='circle'
radius=5
if  shape=="circle":
  print("this is a circle")
  if radius >0:
    print("Cirlcle ha a possitive radius.")
  else:
    print("Invalid radius for a circle.")
else:
  print("unknow shape.")

"""if-elif"""

# Grading system
score =85
if score>=90:
  print("A")
elif 80<= score<90:
  print("B")
elif 70<= score<80 :
  print("c")
elif 60 <= score <70:
  print("C")
else:
  print("F")

# Time of Day
hour =15
if 0<= hour <12:
  print("Good morning!")
elif 12 <= hour<18:
  print("good afternoon!")
else:
  print("Good evening")

# categorizing a number
number=-5
if number>0:
  print("possitive")
elif number <0:
  print("Negative")
else:
  print("Zero")

# checking a user's role
user_role="moderator"
if  user_role=="admin":
  print("You have full access.")
elif user_role =="moderator":
  print("you have limited access.")
else:
  print("you have basic access.")

# sorting therr numbers
a=5
b=10
c=3
if a>b and a>=c:
  print("a is the largest.")
elif b >=a and b>=c:
  print("b is the largest")
else:
  print("c is the largest ")

