# my-varaible=10
# it give the invalid error name
# uninitalized varaibles
#print(my_varaible) # my_varaible is not defind

# varaible Shadowing :
x=10
def my_function():
    x=20
    print(x)
my_function()
# output: 20 

# type error in python 
# x='5'
# y=10 
# result =x+y

# print(result)# it give the type error

# Scope Issue:
def my_function():
    print(x)
my_function()

# Global Variable Modifiction

# x=10
# def my_function():
#     x=20
# my_function()
# print(x)

# Varaible Reassignment:
# x=5
# x="hello"
# print(x)

# varaible Deletion

# x=10
# del x
# print(x)

# mutable Defalut Arguments :
def append_value(value,my_list=[]):
    my_list.append(value)
print(append_value(1))
print(append_value(2))

# Namespace Collision 

import math 
pi =3.14
print(pi)

# vaibel identity check 

# x=[1,2,3]
# y=[1,2,3]

# pirnt(x is y)
# Varible Equalit check 

# x=0.1 + 0.2
# y=0.3 
# print(x==y)


# Varaible initialization with wring types 
# x='hello'
# x=5 

# VArible unpaking Error 
# x,y,z=(1,2)
# print(x)




