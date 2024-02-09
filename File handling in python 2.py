# Need of file Handling 
age=int(input("Enter your age: "))
if age >18: 
    print("Eligible for voting card")
# # Two ways of storing data 
# 1) file handling 
# 2) database 

age=input(input("Enter your data age: "))
f=open("data.txt","r")
print(f.read())
f.close()

