# Three ways to reverse the string 
# 1 using while loop 
# 2 using the for loop 
# 3 using slicing

# reversing the string using while loop 
name="venki"
# r_name=""
# count=len(name)
# while count>0:
#     r_name=r_name+name[count-1]
#     count=count-1
# print(r_name)

# reversing the string using the for  lop 
# r_name=""
# for char in name:
#     r_name=char+r_name
# print("removed string is :",r_name)

# revreversig the string using the slicing 
name=input("enter the string")
print("original string is :",name)
r_name=name[::-1]
print(r_name)