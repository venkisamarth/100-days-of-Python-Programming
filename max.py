numbers=[45,23,23,23,89,45,879,54,98]
max_number=0
for ele in numbers:
    if ele>max_number:
        max_number=ele
print(max_number)

#minimu number in the elements 
numbers=[132,233,43,5,4,22,23]
min_ele=numbers[0]
for element in numbers:
    if element<min_ele:
        min_ele=element
print(f"the min elelmet in the list lis:",min_ele)