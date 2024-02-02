# Global Varaible 
global_var=10 
print(eval("global_var+5"))
#Local Varaible 
def local_example(): 
    local_var=20 
    print(eval("local_var+5"))
local_example()
# usinga Dictionary  for Local Varaible 
local_dict={"a":2,"b":3}

print(eval("a*b",{},local_dict))

# using a Dictionary for Global Varibles 

global_dict={'x':5,"y":2}
print(eval('x-y',global_dict))

#Combing a Dictionary fir global Varaibles

global_dict={'x':4,"y":2}
print(eval('x-y',global_dict))



