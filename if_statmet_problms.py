#check if numbers is positive,negative,or zero
# num=int(input("enter a number"))
# if num>0:
#     print("the number is positive ")
# elif num<0:
#     print("the number is negative")
# else:
#     print("zero")
# check if the number is even or odd

# num=int(input("enter the number :  "))
# if num%2==0:
#     print("even")
# else:
#     print("even")

# check if year is year or not 

# year =int(input("Enter a year"))
# if(year %4==0 and year %100!=0) or (year%400==0):
#     print("leap year")
# else:
#     print("NOt a leap year")

# check if number is divisible by both 2 and 3
# num=int(input("enter the number: "))
# if num%2==0 and num %3==0:
#     print('the number is divide by the 3 and 2')
# else:
#     print("Not divisible by both 2 and 3")

# # Determine the largest of three number 
# num1=float(input("enter first number"))
# num2=float(input("ente the second number"))
# num3=float(input("enter the number"))
# list1=[num1,num2,num3]
# print("the maximum among the three number is:",max(list1))
# check if number is withis a give range
# num=int(input("enter the number: "))
# lower_limit=10
# upper_limit=50
# if lower_limit >= num <=upper_limit:
#     print("wihin the range")
# else:
#     print('out side the range')
# check if the sttring is empty or not
# text=input('enter the stirng you want')
# if len(text)==0:
# #     print("the is the empty")
# # else:
# #     print("this is not the empty stirng")
# # check if student  has passed or failed

# score =float(input("enter the student marks obtainde"))
# passing_score=60
# if score>=passing_score:
#     print("passed")
# else:
#     print("failed")
# # check if the number is prime or not 
# num=int(input("enter the number : "))
# is_prime=True
# if num>1:
#     for i in range(2,int(num**5)+1):
#         if num%i==0:
#             is_prime==False
#             break
#         if is_prime:
#             print("not prime")
#         else:
#             print("Not prime")
#     else:
#         print("Not prime")
# check the given given number is perfect square or not 
# import math
# num=int(input("enter the number:  "))
# if math.isqrt(num)**2 ==num:
#     print("perfect square")
# else:
#     print("Not a perfect square")


# import math

# num = int(input("Enter a number: "))
# if math.isqrt(num)**2 == num:
#     print("Perfect Square")
# else:
#     print("Not a Perfect Square")

# determine the type a traingle based on its sides:
# side1=float(input("enter lenght of side 1:  "))
# side2 =float(input("enter lenght of side 2: "))
# side3 =float(input('enter lenght of side3: '))

# if side1==side2==side3:
#     print("equalateral Triangle")
# elif side1==side2 or side1 ==side3 or side2 ==side3:
#     print("Isosceles Triangle")
# else:
#     print("scalen traigle")

# year=int(input("enter a year:"))
# if year % 100 and year % 400==0:
#     print("leap year and century year")
# elif year % 100 ==0:
#     print("century year but not a leap year")
# elif year %4 ==0:
#     print("leap year but not a century year")
# else:
#     print("Not a leap yar or century year")

# check if the string is palindome:
# word=input("enter  a word")
# if word ==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

month = int(input("Enter the month (1-12): "))
if 1 <= month <= 3:
    print("Winter")
elif 4 <= month <= 6:
    print("Spring")
elif 7 <= month <= 9:
    print("Summer")
elif 10 <= month <= 12:
    print("Autumn")
else:
    print("Invalid month")




