# we can have as if - else statment inside the anothre if-else statment this is called as nesting of if 
#any number of there statments can be neted into one another
# Indentaion is the only way to figure the numer of level in the nesting
# confusion level is more the n avoid the nesting of the if

# sysntax

# if condition:
#     statments
#     statments
#     if condition:
#         statments 
#         statments
#     else:
#         statments
#         statments
# else:
#     statments
# rest of the code
# program for the positive and the negative number
num=float(input("enter the number :  "))
if num>=0:
    if num==0:
        print("the number is zero 0 ")
    else:
        print("enterd number is positive number ")
else:
    print("the enterd number is negative ")
#short hand if 
num=int(input("enter the number: "))
if num>10:print("print he enterd number is greater then 10 ")
# oine line if else 
a=12
b=13
print("hello world") if  a>b else print("welcome")
