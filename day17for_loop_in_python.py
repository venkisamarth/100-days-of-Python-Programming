# -*- coding: utf-8 -*-
"""Day17for loop in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17wjGGEu_jydw3HvGGMxh7zDXmuzb1Eci
"""

for i in range(1,11):
  print(i)

#sum of the numbers divisible by 3 up to 20
sum_divisible_by_3=0
for i in range(1,21):
  if i % 3 == 0:
    sum_divisible_by_3+=i
print("sum of number divisible by 3:", sum_divisible_by_3)

#print sequnce of number up to 5:
for i in range(1,6):
  square=i**2
  print(f"The sequnce of {i} is {square}")

name="venkatesh"
for i in name:
  print(i)

colors=["Red","yellow","white","green"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for i in range(5):
  print(i)

for k in range(1,20,2):
  print(k,end=",")

even_numbers=0
odd_numbers=0
for i in range(1,16):
  if i% 2:
    even_numbers+=1
  else:
    odd_numbers +=1
print("Even number:",even_numbers)
print("odd numbers:",odd_numbers)

# Print elemnt of a lilst great than 5
numbers =[2,8,3,5,678,4,3]
for num in numbers:
  if num>5:
    print(num)

#Calculate the average of numbers in a list:
numbers =[4,7,2,9,5]
total = 0
count= 0
for num in numbers:
  total +=num
  count+=1
average=total/count
print("Avarage:",average)

#print charecters in a string that are vowels
word="hello"
for char in word:
  if char in "aeiou":
    print(char)

for num in range(2,31):
  is_prime="True"
  for i in range(2,int(num**0.50)+1):
    if num %i ==0:
      is_prime=False
      break
    if is_prime:
      print(num)

for i in range(1,6):
  print("*"*i)

#filter the possitive numbers in a list:
numbers=[-2,5,-8,10,-3,7]
for num in numbers:
  if num>0:
    print(num)

