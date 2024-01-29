numbers=[67,86,45,66,54,99,33,54,55,34]
def even_nums(num): 
    if num%2==0: 
        return True
filter_objects=filter(even_nums,numbers)
print(filter_objects)
for ele in filter_objects: 
    print(ele)

numbers=[67,34,546,2323,5454,343,34,334]
filter_objects=filter(lambda num:num%2==0,numbers)
print(filter_objects)
for val in filter_objects: 
    print(val)


filter_object=filter(lambda num:num>=60,numbers)
print(list(filter_object))
 
