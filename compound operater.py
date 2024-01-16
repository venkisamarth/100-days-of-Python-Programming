# a+=b is same as a +=b 
# a+=b not equal to a+b always
a=10
print("value of a:",a)
print("id of a :",id(a))
a=a+10
print("value of a:",a)
print("value of a:",id(a))

a=+10
print("value of a:",a)
print("id of a:",id(a))
a=[10,20,30]
a=a+[40,50]
print("value of a:",a)
print("id of a",id(a))