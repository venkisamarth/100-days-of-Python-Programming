data={"jay":["male",23,2000],"raj":25,"viky":["male",22],"ram":["male",23]}
# count the number of vaue having the numer of value 
# student={"ajay":80,"jay":91,"shantanu":99,"vicky":91}
# print(list(student.values()))
# print(fees[-1]
student={'Ajay':80,"jay":91,"shantanu":99,"viky":91}
name=list(student.keys())
print("last key vlaue pair is:")
print(f"{name[-1]}:{student[name[-1]]}")


data={"jay":["male",23,20000],"ram":["male",23],"raj":43,"vicky":["male",22],"ram":["male",23]}
count=0
for value in data.values():
    if isinstance(value,list):
        count=count+1
print("number of time list occured:",count)
