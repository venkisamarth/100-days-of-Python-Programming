# what is tuple 
# how to create tuple  and use the tuple 
# operations on tuple 
# tuple methods 
# use of tuple 
# diffrence netween tuple and list 

#a tuple  is a collection of items of diffrent types  
#It is nearly similar to the list  in python 
# python list is mutable anf the tuple is imutable 
# python tuple is imutable we can't change the tuple once created 
# what is tuple ?
# a tuple is the collection of items of diffrent data types 


# creating the tuple  

# syntax 

#  tuple_name(item_1,item_2,item_3___item n)
# example :

data =(101,"shantanu", 98.2,[1,2,3,4],(10,20,30))

for ele in data:
 print(ele)
# parantessis are optional 
 data =101,"shatanu",909,343.2,[1,2,34,4],(343,34,45)
#  so tuple is a collection of comma separated values
print(type(data))
print(data)

# creating empty list 
#  syntax :

# tuple_name=(,)

# tuple with single element 
 
tuple_name=("venki",)
print(type(tuple_name))


# tuple paking and the unpaking 
# paking:
t=4,33,"cat"
print(t)
print(t)
print(type(t))


# tuple unpaking 

a,b,c=t
print(a)
print(b)
print(c)

# in tuple every element is represented by index 
# t1=("yes","10",20.4,2+3j,[1,2,3])
# print(t1)
# print(type(t1))

# accessing single element: 

# To access single element of tuple, python uses indexing 
t1=("yes",10,20.4,4,2+3j,[1,2,3])

print(t1[0])
print(t1[2])
print(t1[3])

t=4,3.6,"cat"
print(t[1])
print(t[1:3])


# operations on tuple 

# concatination 

t=(1,2,3,4,5,6)
t1=(7,8,9,10)
print(t+t1)


#tuple repetaion 
t1=(1,2,3)
print(t1*3)

# Deletion 
t1=(1,2,3)
del t1 
# print(t1)

# membership 

t1=(1,2,3)
print(2 in t1)

data =(100,"hello",20.4,[1,2,3,4])
data1=(50,23,49,'yes')
print(data+data1)

var=data+data1
print(id(data))
print(id(var))
data=(100,"hello",20,4,[1,2,3,4])
print(data*3)

print(data)
del data
print(data)












