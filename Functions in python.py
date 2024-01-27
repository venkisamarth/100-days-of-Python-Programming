a=10 
b=20 
a+b
print(a+b)
a=100
b=200
print(a+b)
a=1000
b=2000
print(a+b)

# problem is size of program and hence less efficency 
# less readabality of progam 
# difficalty in managment
# you con't use this code else whre

def add(a,b):
    print(a+b)
add(10,20)
add(100,200)
add(1000,2000)

# what is function 
# a function is a subprogram which are used to perform specofic task having specific logic 

# function are organized block of reusable code 

# you can cal function in any number of times 
# two types of functions 
#  user defined function 
# built in function 

# function  provided by python 
# function predefined by python develepers
# example print() input() len() max() min()

# use defined functions 

# function created by users 

# how create a function
 
# def function_name(parameter):
#     body of function 

def addition(a,b):
    result=a+b
    print(result)

addition(2,4)
#write a function simple_interest  for calculating simple interst 
def simple_interest(p,t,r):
    si=(p*t*r)/100
    print("The simple interest is: ",si)

simple_interest(10000,4,11.23)
simple_interest(40000,5,11.8)
# result=simple_interest(10000,2,2.3)
# print(result)


def add(a,b):
    return a+b
add(1,2)

def muliple(a,b):
    return a*b

def greet(name):
    print("Hello,",name)

def is_even(number):
    return number% 2==0 


def square(number):
    return number **2 

square(20)

def cube(number):
    return number **3 

cube(3)

def average(number):
    return sum(number)/len(number)

# average(23,23)

def is_prime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i ==0:
            return False 
    return False
is_prime(34)
