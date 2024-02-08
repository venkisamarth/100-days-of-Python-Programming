# num1=int(input("Enter the first numbers: "))
# num2=int(input("Enter second number: "))
# div=num1/num2 
# print("rest if the code")

# try: 
#     div=num1/num2 
#     print(div)
# except ZeroDivisionError: 
#     print("divide error Zero is not possible")
# except NameError: 
#     print("rest of code")

# num1=int(input("entere the first number"))
# num2=int(input('Enter the second numbers'))
# try: 
#     div=num1/num2
#     print(div)
# except (ZeroDivisionError,NameError) as obj: 
#     print(obj)
# print('rest of code')
# try
num1=int(input("Enter the first number"))
num2=int(input("enter the second number"))


try: 
    div=num1/num2 
    print(div)
except ZeroDivisionError: 
    print("divide by Zero is not possible ")
print("rest of the code")


