#e#lif in python
#the elif statmente enanles us to check multiple conditions and exicution a specific block of statments
#depending of the upon tree conditon among them 
# Syntax
#  if test/exprestion:
#    # block of code 
#  elif test/expression2:
#    # block of code
#  elif test/expresion:
#     #block of code
# elif test/expresion:
#   # block of code 
# else:
# # block of code executed
num=int(input("enter the number :  "))
if num==10:
    print("the number is 10")
elif num ==20:
    print("the number is 20")
elif num==30:
    print('the number is 30  ')
else:
    print('the number is nut 10,20,30')
    # Grade of the student
marks=float(input("enter the marks student gaine in the exam"))
if marks>85 and  marks<=100:
    print("grade A")
elif marks>60 and marks<=85:
    print("grade B")
elif marks>40 and marks<=60:
    print("grade is c")
else:
    print("Fail")
    
