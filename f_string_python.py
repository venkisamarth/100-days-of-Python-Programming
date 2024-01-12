# f_string statment two parts  
# 1 character "f" or "f"
# 2 string  you want to find 

# syntax 
# f_string 
# name=input("enter the name: ")
# age=input("enter the age: ")
print(f"entertd name is{name} and age is {age}")


# expression in f string 
# print(f{5*5})

# we can all function inside f_string 
def printer(name):
    return "hello"+name
print(f"{printer()}")






