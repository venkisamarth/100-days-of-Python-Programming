# when to use the for loop
# when you know starting point and ending point 
# when you know number of iterations | fixed
# print("using the for loop") 
# for i in range(1,5):
#     print(i)
# i=1
# print("using the while loop")
# while i<5:
#     print(i)
#     i+=1


# 3 when you want to iterate through itrable 
data=[53,45,12,8,9,14,17,11,16,32]
# # write a python  program to for printing even number
# for ele in data:
#     if ele%2==0:
#         print(ele)
# i=0
# while i<len(data):
#     if data[i]% 2==0:
#         print(data[i])
# data={23,45,12,8,9,14,17,11,16,32}
# for ele in data:
#     if ele%2==0:
#         print(ele)
# when to use while loop 
# if you know the number of iterations execution code until user enters yes
# generat random  numbers until you get 15
# when random is importent for us slections sort merging two lists
def findcomplement(num):
    binary=bin(num)[2:1]
    complement=""
    for bit in binary:
        if bit =="1":
            complement+="0"
        else:
            complement+="1"
    return int(complement,2)

findcomplement(5)