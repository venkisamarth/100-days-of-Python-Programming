student ={'name':"John",'age':23,'courses':['Math,"ComSci']}
print(student["name"])
print(student['courses'])
print(student.get("name"))
print(student.get('age'))
student['phone']="5555-5555"
print(student)
student['name']='venkatesh'
print(student)
student.update({'name':'venki','phone':'23343-343'})
print(student)
del student ['age']
print(student)

len(student)
print(student.keys())
print(student.keys())
print(student.values())

print(student.values())
print(student.keys())
for key in student: 
    print(key)


for key,value in student.items():
    print(key,value)


    

