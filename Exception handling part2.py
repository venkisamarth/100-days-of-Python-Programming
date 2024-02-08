#print Exception class object 
# 1 using exception class object 
# 2 using sys module 

# which Exception first 

# example 
num1=int(input('Enter the first number'))
num2=int(input("Enter the secnd number"))
# div=num1/num2 
# print("Division is: ")
# ZeroDivisionError  : name of the Error 
# division by Zero : Exception Information
# try: 
#     div=num1/num2 
#     print("The Division is :",div)
# except ZeroDivisionError as var: 
#     print(var)
#     print(var.__class__)
# print('rest of code')

try:
    div=num1/num2
    print("Division is:",div)
except Exception as var: 
    print(var)
    print(var.__class__)
print("rest of code")

# name and information  another way
import sys 
num1=int(input("Enter the first number"))
num2=int("Enter the second number")
try: 
    div=num1/num2 
    print("Division is:",div)
except: 
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

    

