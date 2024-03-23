# how to unpak the ziped object

student=['jay','jay','vijay']
marks=[90,87,80]
ziped_object=zip(student,marks)
print(list(ziped_object))

stud,mar=zip(*ziped_object)
print(student)
print(marks)

