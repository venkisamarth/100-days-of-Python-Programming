# rais keyword (statmetn)
# An exception can be raied forcefully by using the rais key claues in python 
#raise statments  is used when we wants to thorow  exceptionn for particuler  condition raie

# try: 
#     age=int(input("Enter the your age: "))
#     if age<0: 
#         raise ValueError
#     print("you age is:",age)
# except:
#     print("Enter Valid age")
# print('rest of code')


try: 
    age=int(input("Enter the age: "))
    if age<0: 
        raise ValueError("invalid age")
    print("you age is:",age)
except ValueError as var: 
    print(var)
print("rest of code ")


  
