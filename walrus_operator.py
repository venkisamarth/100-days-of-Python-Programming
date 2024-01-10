# you can assign a value within an expression
# i=0
data=[10,20,30,40,50,60]
# n=len(data)
# i=0
# while i<n:
#     print(data[i])
#     i=i+1
# i=0
# while i<(n:=len(data)):
#     print(data[i])
#     i=i+1

# i=0
# while (i:=i+1)<(n:=len(data)):
#     print(data[i]) 


# i=-1
# while (i:=i+1)<(n:=len(data)):
#     print(data[i]) 

# data=[10,20,30,40,50,60]
# n=len(data)
# while n>0:
#     print(data.pop())
#     n=n-1
# print(data)


# data=[10,20,30,40,50,60]
# while (n:=len(data)):
#     print(data.pop())
#     n=n-1
# print(data)


# while True:
#     ans=input("Do you want to continue(y/n):".lower())
#     if ans!="y":
#        break 
# print("process the request")

while (ans:=input("Do you want to continue(y/n): ").lower=="y"):
        print("process the request")
