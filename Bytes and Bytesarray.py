# data=[224]
# print(bytes(data))

# bytes and bytesarray
# intriduction to bytes and bytearray datatypes 
# How to create these types data?
# some in protant properties 
# advanatges  of bytes data 
# interview of question  and ten

#  bytes datatypes

# 1 bytes =8bit 

# # How to make bytes data
# syntax = bytes (python_object)
data=[10,20,30,40,50]
b=bytes(data)
print(b)
print(type(b))

del data 
for ele in b :
    print(ele)

# the key take way is that when you pass a single integers to bytes(), python object, not the byte value
data=[10,20,30,40]
b=bytes(data)

print(b)

##bytes are immutable 


# bytesarray

data=[10,20,30,40]
b=bytearray(data)
print(type(b))
for b in b:
    print(ele)

# for ele in b:
#     print(ele)

# memory efficiency
import sys
data1=[10,20,40,50,60]
data2=bytes([10,20,30,40,50])
print(sys.getsizeof(data1))
print("memory consumed by data2:",sys.getsizeof(data2))





