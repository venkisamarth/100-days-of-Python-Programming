# why module 
# In any project we have to write big program It becomes difficult to manage and organize 
# program

# so we break down big program into small managable and organized files having same logic These files are nothing but 
# modules

# It provieds reusability to our code 
# what are modules i python?
# a file containg python code is called as python module
# module contains fucnions definations ,class defination ,varaible code python  statemts you want to include  in your python main file
import addition
print(addition.add(3,5))
# print(addition.subtract(534-23))
print(addition.mul(3,5))

print(addition.subtract(3,5))

print(addition.subtract(234,23))
# import with rename
import addition as a
a.add(3,5)
a.subtract(234,23)
a.mul(234,23)

a.subtract(23,234)

a.add(23,23)

from addition import add
add(23,343)

# importing the all 
from addition import*
from addition import add,mul
add(12,12)
mul(10,10)

# there are two types of moduls 
#1 is user defined module and another one is Built in module
import math
print(math.factorial(5))
import math as m 
import addition
import addition
