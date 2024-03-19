# Numpy is the short from of Numerical Python 
# In 2005 ,Travis oliphant created Numpy  pakage
# Numpy is a pakage that defines a multi-dimentional array object and associative fast math function that 
# operate that operate on 
# It also has funciton for working in domin of linear algibara Fourier Transformation and Matrices 
#In sample words. it is the fundamental pakage for scintific  in python 

#2 what are array 
#1 An array is defined as a collection of items that are stored at contiguous memory locations 
# It is a contains which cah hold a fixed  number of items, and thes should these should be of the same type 
# A combination of array saves a lot of times The array can reduce  the over  rall size of the code 


# 3 Advanatages  of using numpy array 
# 1> Numpy  uses much less memory to store data 
# 2> Numpy makes it externaly easy to perform  mathematical  operations  on it 
# 3> used for the creation of n_dimational  array 
# 4> Finding  elements in Numpy array is eassy 
import builtins

# Get all attributes of the builtins module
builtin_attributes = dir(builtins)

# Filter out the functions from the attributes
builtin_functions = [attr for attr in builtin_attributes if callable(getattr(builtins, attr))]

# Print the list of built-in functions
for func in builtin_functions:
    print(func)