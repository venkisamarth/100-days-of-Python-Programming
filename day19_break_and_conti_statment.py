# -*- coding: utf-8 -*-
"""Day19 break and conti statment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fpz5PqpCoJa6jEqWHKk9gnHkIg4oh5ja
"""

# A while loop can vontain for loop iside it here are  the 10 example
# Example1: Basic number printing
x=1
while x<=3:
  for i in range(3):
    print(x,i)
  x=x+1

num=2
while num<=5:
  for i in range(1,11):
    print(f"{num}x{i}={num*i}")
  num=num+1

num = 2
while num <= 5:
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    num += 1

row=1
while row<=3:
  for col in  range(1,4):
    print("*",end=" ")
  print()
  row+=1

# sum of numbers
sum_result=0
count=1
while count <=5:
  for i in range(1,count+1):
    sum_result+=i
  count+=1
print(f'sum:{sum_result}')

# nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=0
while row <len(matrix):
  for col in range(len(matrix[row])):
    print(matrix[row][col],end=" ")
  print()
  row+=1

# #prime numbers
# num=2
# while num<=10:
#   is_prime=True
#   for i in range(2,num):
#     if num % i == 0:
#       is_prime=False
#       break
#     if is_prime:
#       print(num,"is prime")
#     num+=1

char = 'A'
while char <= 'C':
    for i in range(3):
        print(char, end=" ")
    print()
    char = chr(ord(char) + 1)

# Facorial
num=1
while num<=5:
  factorail =1
  for i in range(1,num+1):
    factorail=factorail*i
  print(f"factorail of {num}:{factorail}")
  num+=1

a,b=0,1
while a<10:
  for _ in range(5):
    print(a,end=" ")
    a,b=b,a+b
  print()

# countdown Timer
time_left=5
while time_left>0:
  for sec in range(time_left,0,1):
    print(f"The left:{sec} seconds")
  time_left-=1

# Break in For loop
for i in range(5):
  if i ==3:
    break
  print(i)

num=0
while num<5:
  if num==3:
    break
  print(num)
  num=num+1

# continue in for loop
for i in range(5):
  if i==2:
    continue
  print(i)

# continue in while Loop
num=0
while num<5:
  if num ==2:
    num=num+1
    continue
  print(num)
  num=num+1

# Break statment in Nested  Loop
for i in range(3):
  for j in range(3):
    if j ==1:
      break
    print(i,j)

# continue in Nested Loop
for i in range(3):
   for j in range(3):
    if j ==1:
      continue
    print(i,j)

# Brake in  list Iteration
numbers =[1,2,3,3,5]
for num in numbers:
  if num== 3:
    break
  print(num)

#Continue statment  in a list Iteration
numbers=[1,2,3,4,55,5]
for num in numbers:
  if num==3:
    continue
  print(num)

# while True:
#     user_input = input("Enter a number (or 'exit' to stop): ")
#     if user_input.lower() == 'exit':
#         break
#     print(f"You entered: {user_input}")

for i in range(10):
  if i %2==1:
    continue
  print(i)

"""How to emulate the do while loop in python



Python doesn't have a built-in do-while loop like some other programming languages, but you can achieve similar functionality using a while loop with a conditional break. Here's an example of how you can emulate a do-while loop in Python:
"""

while True:
  user_input=input("Enter 'exit' to stop :")
  if user_input.lower()=="exit":
    break
  print(f"You entered:{user_input}")

"""In this example, the loop will always execute at least once, and then it will check the condition (user_input.lower() == 'exit') at the end of each iteration. If the condition is met, the loop will exit; otherwise, it will continue. This is a common pattern to achieve the behavior of a do-while loop.

The break statement is used to exit the loop when the desired condition is met. Note that using break in this way can make the code less readable, so it's essential to use it judiciously.
"""

