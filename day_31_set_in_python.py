# -*- coding: utf-8 -*-
"""Day 31 set in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KxGPd7G40hlZBpC7yBCDMyTBlwsdo-A0
"""

s={2,4,2,6}
print(s)

info={"Carla",19,False,59,19}
print(info)

harry=set()
print(type(harry))

for value in info:
  print(value)

# creating the set
my_set={1,2,3,4,4}
print(my_set)

# adding the element s:
my_set.add(6)
my_set.update({7,8,9})

# Removing the element
my_set.remove(3)
my_set.discard(10)

# Set Operations:
set1={1,2,3,4}
set2={4,5,6,7}
union_set=set1.union(set2)

print(union_set)

# checking the Membership
squared_set={x**2 for x in range(1,6)}
print(squared_set)

# copying a set
copy_set=my_set.copy()

print(copy_set.copy)

frozen_set=frozenset([1,2,3])
print(frozenset)

# set Methods:
set_length=len(my_set)
popped_element=my_set.pop()

print(popped_element)
