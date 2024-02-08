# class FiveDivisionError(Exception): 
#     "this is exception class called when five divison  Error happens"
# try: 
#     n1=int(input("Enter the first number"))
#     n2=int(input("Enter the secode number"))
#     if n1==5: 
#         raise FiveDivisionError ("cannot divide by five")
#     div=n1/n2
#     print("division is :",div)
# except(FiveDivisionError,ZeroDivisionError) as var: 
#     print(var)
# print("rest of the code")

class FiveDivisionError(Exception): 
    "this is the FiveDivisionError "
try: 
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    if n2==5: 
        raise FiveDivisionError("cannot divid by zero")
    div=n1/n2 
except (FiveDivisionError,ZeroDivisionError) as var: 
    print(var) 





