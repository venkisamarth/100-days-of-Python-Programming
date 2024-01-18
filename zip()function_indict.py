#the purpose of zip() function is to map similar index of multiple container
student ={"jay","jay","viru"}
roll={101,102,103}
# return the single iterator having mapped values form all contains

zip_object=zip(student,roll)
print(zip_object)
for item in zip_object:
    print(item)


# example02= converting to list 

student=["jay","raj","viru"]
roll={101,102,103}
zip_object=zip(student,roll)
print(zip_object)
print(list(zip_object))

print(dict(zip_object))
print(set(zip_object))

student=["jay","raj","viru","shantahanu"]
roll=[101,102,103]

marks=[34,56,78]

zip_object=zip(student,roll,marks)
print(list(zip_object))

id=[1,2,3,4,5]
vowels="aeiou"
print(list(zip(id,vowels)))


jay={"java":80,"python":100,"oop":91,"computer_network":89}
raj={'java':89,"python":89,"oop":89,"computer_network":100}
shanthanu={"java":100,"python":100,"computer_newtork":100}
marks=[]
student_list=[jay,raj,shanthanu]
for student in student_list:
    sum1=0
    for item in student:
        sum1=sum1+student[item]
        percentage=sum1/len(student)
        marks.append(percentage)

print(marks)
student_name=[jay,raj,shanthanu]
print(list(zip(student_name,marks)))

    