# What is type conversion  in python
"""type  converting  the value of one data type to another data type is called type casting or type conversion"""
# Two types of conversion 
# 1) implicit type conversion
# 2) Explcit conversion

# Implicit conversion 
# In imlicit type conversion on python automatically converts one data type to the another data type 
# Generally  python promts conversion of lower datatype to avoid data loss
# imlicit  type conversion
# x=123
# y=1.23
# z=x+y
# print(z)

# Explicit conversion
x=123

# y=int(input("enter the numbers"))
# z=x+y
# print(x+y)

# explicit  type conversion 
# programmer converts one data type to another data type
# we have predefined funcion for explicit  type conversion

# function
# int(value)
# float(value)
# str(value)
# complex(value)
# list(value)
# tuple(value)

# typecosting in python
# int,float,complex- primitive datatype
# str,list ,tuple -sequancial data type

# float to int 
value=12.5
print(value)

type(value)
value1=int(value)
print(type(value1))
print(value1)

# String to int 
value="12"
print(type(value))
value1=int(value1)
print(type(value1))

# int to float
value=12
print(value)
value1=float(value)
print(value1)

# str to float
# Note inside floating point number complex
value="12.3"
print(type(value))
value1=float(value1)
print(value1)

# int to str
value=12
print(type(value))
value1=str(value)
print(value1)

# str to list 
value="hello"
print(type(value))
value=list(value)
print(type(value))
print(value)

# str to tuple
value="venkatesh"
print(type(value))
value=tuple(value)
print(type(value))
print(value)

