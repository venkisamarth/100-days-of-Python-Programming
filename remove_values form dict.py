# using del keword 
# usng clear() method 
# using pop()
# using popitem()
# using Dictionary comprehension

# using del keyword 
# del keyword is used to delete the object in the python 
# this method remove a dictionary  item  
# syntax 
# del dict dict_name[key]

student ={"gabber":20000,"thakure":15000,"basanti":14000,"viru":10000}
del student 
# print("after deletion",student)
student = {'gabber':20000,"thakure":15000,"basanti":14000,"viru":10000}
del student["basanti"]
print("after deletion",student)

#del student['basanti']
name=input("enter student name: ")
if name in student:
    del student[name]
else:
    print("not such student present")
# using the clear method()

# to remove all the item from the dict  
# it return empty dictionary 
#  syntax  
#    dict_name.clear()
    
student ={'gabber':20000,"thakure":15000,"basanti":1400}
print(student )
student.clear()
print(student)


