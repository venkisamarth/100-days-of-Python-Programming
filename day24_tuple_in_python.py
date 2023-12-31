# -*- coding: utf-8 -*-
"""Day24 tuple in python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L5cIdTBy8OeMDBiojV_LPCW56pmhmoXM

Tuple

A tuple in Python is similar to a list but is immutable, meaning its elements cannot be changed or modified after the tuple is created. Tuples are defined using parentheses ().
"""

numeric_tuple=(1,2,3,4,5)
 print(numeric_tuple)

"""Mised Data types Tupe:"""

Mixed_tuple=("apple",3.142,True,42,"banana")
print(Mixed_tuple)

"""Nested Tuple"""

nested_tuple=("john",(25,"male"),["Python","Java","javascript"])
print(nested_tuple)

"""Empty Tuple:"""

empty_tuple=()
print(empty_tuple)

"""single -Element Tuple:"""

single_element_tuple=(42,)
print(single_element_tuple)

# NUmaric Tuple:
numeric_tuple =(1,2,3,4,5)
for element in numeric_tuple:
  print(element)

# Mixed Data Types Tuple:
mixed_tuple = ('apple', 3.14, True, 42, 'banana')
for element in mixed_tuple:
    print(element)

# Nested Tuple:
nested_tuple = ('John', (25, 'male'), ['Python', 'JavaScript'])
for element in nested_tuple:
    print(element)

# 4. tuple of string:
string_tuple=("hello","world","python")
for element in string_tuple:
  print(element)

# tuple with single Element:
single_element_tuple=(42,)
for element in single_element_tuple:
  print(element)

# tuple Unpaking:
pairs_tuple=((1,"one"),(2,"two"),(3,"three"),(4,"four"))
for number,word in pairs_tuple:
  print(f"{number}:{word}")

# Enumerating elements:
colors_tuple=("red","green","blue")
for index, color in enumerate(colors_tuple):
  print(f"Index {index}:{color}")

# using Range and Len:
numersic_tuple=(10,20,30,40,50)
for i in range(len(numeric_tuple)):
  print(numersic_tuple[i])

for i in numersic_tuple:
  print(i)

# tuple with Repeted Elemets:
repeated_tuple = ('a',) * 3
for element in repeated_tuple:
    print(element)

# Iterating Over Tuple Inside a Tuple:
nested_tuple=((1,2,3,4),("a","b","c","d"),("python","java","javascript"))
for inner_tuple in nested_tuple:
  for element in inner_tuple:
    print(element)

