# list is a comma separeted values in square breacekets in [] is compalsary
data=['jay',23,40039]
# tuple is a comma sparated values in paranthesis is separated paranthisis is optional

data='jay',"venki",23.3,343
print(tuple)
print(type(data))

l=["hello",12,23.5,2+4j]
t=("hello",12,23.5,2+4j)


# mutability
# list is mutable 

# tuple is immutable 

l=["hello",12,23.5,2+3j]
my_tuple='hello',12,23.5,2+3j

l[1]=20
print(l)
# t[1]=20
# print(my_tuple)

# memory consumption 
# tuple take less memeory compared to the list 
# list take more memory than tuple 
import sys
l=['hello',12,25.3,2+3j]
my_tuple=("venki",34,23.3,4+4j)

print(sys.getsizeof(l))
print(sys.getsizeof(my_tuple))