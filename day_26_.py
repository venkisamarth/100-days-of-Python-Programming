# -*- coding: utf-8 -*-
"""Day 26  .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AD8jgm019wx8FlJEx3Na-oqkqAkgLU0c

Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
"""

import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")

