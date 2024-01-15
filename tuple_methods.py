# length of tuple 
# len() function  is used  find the len or the number of element in the tuple 
# syntax 

# len(tuple_name)

# example 

t=("hello",100,20,4,[1,2,3])
print(len(t))
data =(100,"hello",20,4,[1,2,3,4])
print(len(data))

print("The length is:",len(data))

# count() method:

# count occurence of particuler element in tuple 

# syntax 

t=("s","h","a","n","t","a","n","r")
print(t.count("s"))
data=(100,"hello",20,4,"hello",[1,2,3,4])
print('count of hello is:',data.count("hello"))

# index() method 

# return index of passed element 

# syntax 
# tuple_name=name.index(element)

# t=tuple_name.index(element)

# print(t)

s='shanthanu'
t=tuple(s)
print(t)
print(type(t))

print(t.index("s"))

print(t.index("a"))

data=(100,"hello",20.4,"hello",[1,2,3,4])
print('count of hello world is ',data.count("hello"))


# max() function

# for indexing maximum in tuple 
# syntax 
# max(tuple_name)

# my_tuple=(1,2,3,4,5)
# print(max(my_tuple))

# print("*"*3)


# min() function for the mimimum in tuple syntax :
#     min (tuple_name)

# data=(93,34,343,6645,890,4,4)
# print(min(data))

# data="sachine","shanthanu","hello","yess"

# print(max(data))

# print(min(data))


# importance of tuple 

# how to iterate over tuple 
data=('sachin',100,"shanthanu","hello")
for ele in data:
     print(ele)

# while ele in data:
#     print(ele)
#     if ele=="hell":
#         break 
     
index=0
while index<len(data):
        ele=data[index]
        print(ele)
        index=index+1
     
my_tuple=(1,2,3,4,5)
index=0
while index <len(my_tuple):
     element=my_tuple[index]
     print(element)
     index=index+1
     

# how to access the nested tuple 
data='sachine',"100","shantanu","venki"
for ele in data:
      print(ele)
index=0
while index <len(data):
      ele=data[index]
      print(ele)
      index=index+1

data=("venki","sachin",[1,2,3,4])

print(data[2][2])




