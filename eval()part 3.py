# using the global Dictionary in python 
x=10 
global_dict={'x':x}
print(eval("x",global_dict))

# using the Local Dictionary only
local_dict={"x":5}
print("x",{},local_dict)

#using the local Dictionary and the global Dictionaries separately 
x=10 
local_dict={'x':5}
global_dict={'x':x}
print('x',global_dict,local_dict)


# using Both Globa and local Dictionaries with overlaping keys
x=10 
local_dict={"x":5}
global_dict={"x":x}
print(eval("x+x",global_dict,local_dict))

#using global Dictinary with Varaible created inside a fucniton 
def my_function(): 
    y=3 
    global_dict={"x":5}
    return eval("x+y",global_dict)
print(my_function)

# using Local Dictioary with VAraible inside a Fucntion 
def my_function(): 
    x=5 
    local_dict={'y':5}
    return print(eval('x+y',{},local_dict))
print(my_function)

# using global and local Dicatonaries with Varaible created inside a Fuction 
def my_function(): 
    global_dict={'x':5}
    local_dict={'y':3}
    return eval("x+y",global_dict,local_dict)
print(my_function)