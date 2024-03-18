#A list cannot directly handle mathematical operations,while array can 
#An array consumes less memory than a list  
# using am array is faster than a list 
# a list can store diffrent  datatypes  while you can't do that in an Array
# A list is easier  to modify  since a list store  each ellements  indviduvaly ,it  is easier to add  
#and delete an elements than an array does 
# In list one elemets can have nested data with diffrence size ,while you cannot do the  same in array 
# array homogenous 
#list are hetrogeneous 

# create a numpy array with radom interger in rage  0-100 and the size be  25 
import numpy as np 
a=np.random.rand(0,100,25)
print(a)

#create a numpy array with a shape 3x3 that has all elementsas 1 
arr1=np.ones((3,3))
print(arr1)
#create a numpy array in the shape 2x3 with random integer in range of 0-100
#reshapthe array in the shape 3x2 

# arr=np.random.random(0,100,(2,3))
# print(arr) 
# create a 2x3 array of random interger between 0 and 100 
import numpy as np

# Create a 2x3 array of random integers between 0 and 100
# arr = np.random.randint(0, 101, size=(2, 3))

# Reshape the array to shape 3x2
# arr_reshaped = arr.reshape(3, 2)

# # Print the updated shape
# print("Updated shape:", arr_reshaped.shape)

# arr= np.random.randint(0,101,size=(2,3))
# print(arr)
# reshaped_arr=arr.reshape(3,2)
# print('The updated array is:',reshaped_arr)

#create a random array with a range 0-100 with a size of  50 
arr=np.random.randint(0,101,50)
print(arr)

print(arr[0:11])
print(arr[40:])
print(arr[10:26])
print(arr[22])
print(arr[::-1])
print(arr[-1:-11:1])
print(arr[-1:-11])
arr2=np.array([1,2,3,4,5])
# insert the element at the end of the arr
print(arr2)
arr2=np.append(arr2,6)
print(arr2)

#insert 10 at the begening 
arr2=np.insert(arr2,0,10)
print(arr2)

# creating the array using the diffrence function 

# arrange():
a=np.arange(0,5,2,dtype=float)
print(a)

import numpy as np 
arr=np.arange(1,6)
print(arr)
print(np.arange(1,6,dtype=float))
print(np.arange(6))
print(np.arange(1,6,2))

print(" The zero function ")
print(np.zeros(6))
print(np.zeros((2,3)))
print(np.zeros((5,5)))
a=np.zeros((2,3))
print(a)


print(np.ones((6,3)))
print(np.ones(2))
print(np.ones((2,3),dtype=int))

print(np.full((2,3),4,dtype=int))
print(np.full(4,8,dtype=float))
print(np.full(5,0,dtype=float))

# reshape(): 
arr=np.arange(0,100)
print(arr)
print(arr.reshape(25,4))

print(np.full((2,3),4,dtype=float))
print(np.full(4,8,dtype=float))

print(np.arange(6).reshape(2,3))

print(np.arange(50).reshape(25,2))

arr=np.array([1,2,3,5,6])
print(arr)
arr=np.insert(arr,4,30)
# insert 30 before 4 
print(arr)

#update ele 5 to 50 
# arr[6]=50
# print(arr)
# arr=np.delet(arr,3)
# print(arr)

#create a function to serch elements 30 

def serch(arr,i): 
    if i in arr: 
        print('yes the element is present')
    else: 
        print("No such element i present ")

serch(arr,50)

