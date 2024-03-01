#lobal Variable: 
# Global VAriable 
x=10 
def print_global(): 
    print("Gloabal varaible x inside fucntion:",x)
print("Gloable variable x outside funciton:",x)

print_global()

# Local Variable: 
def print_Local(): 
    # Local Variable 
    y=20 
    print("local vraible y inside funciton:",y)
# This will raise an error because y is local to the 
# print("local vraible y outside funciton:",y)


# intermediat Example: 
# Goable and Local Variable interaction: 
# # gloable varaible 
x=10 
def modify_global(): 
    # Trying to modify gloable variable x 
    global x 
    x+=5
    print("modify gloable variable x inside funciton:",x)
modify_global()
print("Gloable variable x outside funcito after modfication:",x)


# Local Variable sadowing: 
# Global Variable 
x =10 
def shadow_variable(): 
    # Local variable with the same na,e as gloable variable 
    x=5
    print("Local varibale x inside funciton:",x)
shadow_variable()
print("Global vvariable x outside function:",x)

# Advanced Exampls : 
# Nested Fucniton and Variable scopes:

def outer_funciton(): 
    #Local Variable in outer function
    outer_var=10 
    def inner_functoin(): 
        nonlocal outer_var 
        outer_var +=5 
        print("outer variable outside inner funciton:",outer_var)
    inner_functoin()
    print("outer variable outside inner fucntion:",outer_var)
outer_funciton()
# Gloable variable 
x=10 
def reassign_gloable(): 
    #Reassigning Gloabal vraible
    global x 
    x=20 
    print("REassigned gloabl variable x inside funciton:",x)
reassign_gloable()
print("Reassigned Global varaible x inside fucniton:",x)
reassign_gloable()
print("Gloabl variable x outside fucniton after reassign:",x)