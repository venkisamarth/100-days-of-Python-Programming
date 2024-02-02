# eveal() function a built in function used in python  
# # eval function parses the strings arguments 
# and evaluate it as a python expresion  
# string - as a python Expression 

# syntax of eval()

# eval(Expression,global=None,locals=None)

# it returns value of eval(())

# result of Expression present in string argument 

num=3
var=eval('num*num')
print(var)

num=3
var=(eval("num*num"))
print(type(var))
print('The eval function accept the string only  as the parameter')
var=eval("print('hello world')")
print(var)

var=eval("[1,2,3,4],[1,2,3,4]")
print(var)

# data=eval(input("enter the value of the x :"))
# ans=eval("x*(x+2)")
# print(ans)

equation ='2+3*4'
result=eval(equation)
print(result)

equation='2**3'
result=eval(equation)
print(result)

import math
equation='math.sin(math.radians(30))'
result=eval(equation)
print(result)

equation='math.sqrt(23)'
result=eval(equation)
print(result)

# whrer the eval funcion mostly used 
# to take inputs 
# if the user wants to evaluates the string into code then can eval function 
def password():
    print("Secret password is 1234")

def solve_eq():
    eq = input("Enter the equation in the form of x: ")
    x = int(input("Enter the value of x: "))
    ans = eval(eq)
    print("The solution:", ans)

password()  # Call the password function to display the password
solve_eq()  # Call the solve_eq function to solve the equation






