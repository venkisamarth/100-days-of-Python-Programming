# special operators in python 

# # what are python's special Operators 

# - Membership Operators in python 
# - How membership Operators works on dictionaly 
# - identity operators in python 
# - diffrenct between == and = operators 


# Two types of special Operators 

# Membership operators 
# Identity Operators 

str1="shanthanu"
tanu='a'
print(tanu in str1)
print("s" in str1)

numbers =[10,20,30,40,50]
print(50 in numbers)

print(50 not in numbers )

print(60 in numbers )
print("50" in numbers)

# group =['aman', 'pratik','raj']

# name=input("Enter the name")# raj
# if name in group: 
#     print(f"{name} is presnt " )
# else: 
#     print(f"{name} is not present")
#in operators in used in conditions in python 
# True :- specified value is the member of  sequnce 
# False:- Not a member of 

# not in operators 
# True:- if sepcified valur is't member ofsequnce 

# false  if the specified operators is in sequnce 
# How membership ooperators workd on dictionaty and trickky questions? 

#in membership operators keys or checked in the membership operatots 
# data={1:"shantanu",2:'jay'}
# print("shantanu" in data)
# print(1 in data)

# # in dictionary the value is searhed on the basic of the  key if that keys or not found then it should be return the false 
# lst =[1,2,3]
# print(lst in lst)

# identity Operators? in python

#identity Operatoros comparision id's of the objects 

# used to know objects are same or not 
# Two membership Operators 

# is 
# is not 

a= 100 
b=100 
c="shanthanu"
print(a is b)# is compares id(a) == id(b)
print(a is c)

# Diffrence between is Operators and == Operators 

a=100 
print(id(a))

b=100 
print(id(b))
print(a == b)#True   100 == 100 
print(a is b)# id(a)== id(b)




























