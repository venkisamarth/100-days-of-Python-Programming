# expression for varaibles inn iterable of cind1 if neted varaible 
# syntax 

# [expression if condition  else expression for varaible in iterable]

# nums=[3,6,12,14,15]
# sq=[]
# for num in nums:
#     sq.append(num*num)
# print(sq)

# print("using the  list comprehension")
# print([num*num for num in nums])

# nums=[3,6,8,12,14,15]
# sq=[]
# for num in nums:
#     if num%2==0:
#         sq.append(num*num)
# print(sq)

# print("using the list comprehension")
# print([num * num for num in nums if  num %2==0])
# print('*'*10)
# nums=[3,4,5,6,7,8,9,10]
# sq=[]
# for num in nums:
#     if num%2==0:
#         if num%3==0:
#             sq.append(num*num)
# print(sq)

# print("using the list comprehension")
# print([num*num for num in nums if num%2==0 if num%3==0])

# nums=[3,6,8,12,14,15]
# result=[]
# for num in nums:
#     if num %2==0:
#         result.append(num*num)
#     else:
#         result.append(num*num*num)
# print(result)

# print('using the list comprehension')
# print([num*num if num%2==0 else num*num*num for num in nums])

# nested for loop 
# lst=[]
# for num  in range(3,6):
#     for j in range(5,7):
#         lst.append(i*j)
# print(lst)
# print('$'*3)
# print([i*j for i in range(3,6) for j in range(5,7)])

# num=int(input("enter a numbers:  "))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("Zero")
# print("positive" if num>0 else 'negative' if num<0 else "Zero")


# if else in list comprehension
    
# nums=[90,0,-34,33,-21,20]
# status=[]
# for num in nums:
#     if num>0:
#         status.append("positive")

#     elif num<0:
#         status.append("zero")
#     else:
#         status.append('zero')
# print(status)
# print('positive' if num>0 else 'negative' if num>0 'zero' for num in nums)

ages=[23,78,16,43,21,17,12,48]
checkup_fees=[]
for age in ages:
    if age<18:
        checkup_fees.append(100.0)
    elif age<30 and age>=18:
        checkup_fees.append(500.0)
    elif age<45  and age>=31:
        checkup_fees.append(700.0)
    else:
        checkup_fees.append(200.0)
print(checkup_fees)
print("using the list comprehension")


print([100.0 if age<18 else 500.0 if age<30 and age>18 else 700.0 if age<45 and age>=31 else 200.0 for age in ages])
        









