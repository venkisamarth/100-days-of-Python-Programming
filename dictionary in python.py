# what is dictionary in python
# how to create dictionary?
# characterstiecs of dictionary
# Dictionary an unorder collection of key value pairs  

# example
emp_data={"name":"venki","age":21,"salary":18000}
print(emp_data)

#Two types two reate the dictionary 

#using curly braces: 

dic_name={"key1":"value1","key2":"value","key3":"value3"}
#using dict() function

# first way 
student ={"name":"jay","roll":101,"marks":86.2}
print(student )
print(type(student))

# second way 

student =dict([("name","jay"),("roll",101),("marks",23)])
print(student)
print(type(student))


# charaterstircs of Dictionary

# keys must be immutable items (string,tuple,...etc)
# values can be any:not allowed
# dictionary is immutable
student ={"salary":10000,"name":"vaki","salary":123343}
print(student)

employee={"salary":10000,"name":"ram","salary":2322323}
print(employee)
# student={[1,2,3]:"hello"}
# print(student)

# empty dictionary
student={}
print(type(student))
print(student)

# some importent points abouts dictionary
# some importance points about dictionary
# Finding length of dictionary 

# Dictionary
# is unorderd 
# keys can't be duplicated but values can be dulicated

# keys are case-sensitive 
employee={"suraj":120000,"karns":70000,"Suraj":30000}
print(employee)
employee={"suraj":120000,"karna":70000,"suraj":30000}
print(employee)

# keys are sensitive 

emmployee={"venki":23324,"raju":2345353,"rani":23243,"Rani":2323232}
print(employee)

#lenght of dictionary
employee={"suraj":122323,'venki':93993,"suraj":34343}
print(len(employee))
count=0
for key in employee:
    count=count+1
print(count)

# accessing the dictionary item 
# we cannot use indexing and slicing on Dictionary
# syantax =
# dict_name[key]
employee={"venki":2323,"raju":343,"nami":4545}

employee["venki"]

print(employee["venki"])
