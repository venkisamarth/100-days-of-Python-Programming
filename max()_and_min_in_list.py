# find the maximu and the minimum in the list we can use an inbult method of list ie max()

# systax 
#    max(iterable,key,default)
# iterable =an iterable such asa list 
# key(operionl)= basis for compalrsion 
# # default def value is given itreable is empty

# numbers=[3,2,8,9,10,8,3]
# print(max(numbers))

names=["shanthanu",'Rohen','Adity','karthik']
print(max(names,key=len))

# Finding the maximum vlaue in a list
numbers = [4,5,8,9,2,10]
max_value=numbers[0]
for num in numbers:
    if num>max_value:
        max_value=num
print(f"the maximum value is :{max_value}")

#find the mimimum value in the list 
numbers =[5,8,9,10,3]
min_value=numbers[0]
for num in numbers:
    if num <min_value:
        min_value = num 
print(f"the minimum value is: {min_value}")
