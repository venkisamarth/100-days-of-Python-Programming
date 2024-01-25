# syntax 
# {key:value for (key:value) in iterable}

nums=[1,2,3,4,5]
print({num:num*num for num in nums})
print("using the for loop")
my_dict={}
for num in nums:
    my_dict[num]=num*num
print(my_dict)


my_dict={}
for num in nums:
    if num%2==0:
        my_dict[num] =num**2
print(my_dict)

print({num:num**2  for num in nums if num %2==0})


str1="cOding"
my_dict={}
for char in str1:
    my_dict[char.upper()]=(ord(char),ord(char.swapcase()))
print(my_dict)

#print({char.upper():(ord(char),ord(char.swapcase()) for char in str1)})
# set comprehension
nums=[1,2,3,4,5]
print({num**2 for num in nums})



