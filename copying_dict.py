# using =operater
# using copy() mehtod

# create new copy of dicationary and return it Syntax 

# dict_name.copy()
old_student= {"karna":12000,"jesan":3000,"john":14000}
new_dict=old_student
print(new_dict)
print(id(old_student))
print(id(new_dict))


# using the copy() method()
old_student={"karna":12000,"jeson":3000}
new_student=old_student.copy()
print(new_student)
print(old_student)
print(id(old_student))
print(id(new_student))


