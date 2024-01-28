# positional arguments 
 #you have to maintain positions (orders) of arguments
# number of parameter must be equal to number of arguments 
# positions must be maintained 
def power(a,b):
    print(a**b)
power(2,3)
power(3,2)
print(complex(4,5))
print(complex(4,6)) 

# number of parameter mustbe == number of arguments 

# power(2,3,4)
# power(23,3,4)
# power(1)

# simple addition function 
def add(x,y):
    return x+ y 
result =add(5,7)
print(result)
# calculate the area of the rectangle 
def calculate_area(lenght,width):
    return lenght * width

area=calculate_area(42,45)
print('the area of the recatangle is: ',area)
# Exponetial Function 
def power(base,exponent):
    return base**exponent
result =power(2,4)
print('The exponet of the number is: ',result)
#List concatenation : 
def concatenation_list(list1,list2):
    return list1 +list2
result =concatenation_list([1,2,3],[4,5,6])
print(' the concatenated string is : ',result)

#Circle Area calculation 
import math 
def calculation_circle_area(radius):
    return math.pi * radius**2 
area =calculation_circle_area(3)
print("Area of circle with radius 3",area)
# Simple interest calculator 
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si 
result =simple_interest(1000,1,22)
print('The simple interest is :', result)

# Traingle area calculation 
def calculate_triangle_area(base,height):
    return 0.5* base * height
area =calculate_triangle_area(4,6)
print('The ara of the traingle is:',area)
#quadratic Equation solver:
def solve_quadratic(a,b,c):
    discrimenent =b**2-4*a*c
    if discrimenent<0:
        return "No real roots"
    elif discrimenent==0:
        root=-b/(2*a)
    else: 
        root1=(-b+math.sqrt(discrimenent))/(2*a)
        root2=(b+math.sqrt(discrimenent))/(2*a)
        return root1,root2 
roots =solve_quadratic(1,-3,2)
print("Roots of the quadratic equation :",roots)
# Temperature converter 
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperature_f = celsius_to_fahrenheit(30)
print("Temperature in Fahrenheit:", temperature_f)
