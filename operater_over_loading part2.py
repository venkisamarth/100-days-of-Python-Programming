# what is operater overloading 
# when some operater behaves diffrently depending on values is called as operator overloding 
# you can also assign a new value meaning to operators also and you can extent funcionality of operator 
# you can change default behaviours  of operators using over_riading 

num1=10 
num2=20 
print(num1.__add__(num2))
print(int.__add__(num1,num2))
print(dir(int))
# first it check the datatype of the left operand 
# go on that class 
# call__add__(function)
num1="23"
num2="23"
print(num1+num2)

print(num1.__add__(num2))
print(str.__add__(num1,num2))
print(dir(int))