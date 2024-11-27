# # courses=['Histrory','math','Physics','compsci']
# # print(courses)
# # # print(len(courses))
# # # print(courses[0:2])
# # # print(courses[0:3])
# # # print(courses[0:4])
# # # print(courses[-1])
# # # print(courses[-2])
# # # print(courses[3])
# # # print(courses[0])
# # print(courses[0:2])
# # print(courses[:2])
# # print(courses[2:])
# # # list methods in python 
# # # the first method of adding the element to the list is given by bellow
# # # uppend mehtod 
# # courses.append('Art')
# # print(courses)
# # courses.insert(0,"art")
# # print(courses)
# # courses_2=['art','education']
# # print(courses_2)
# # courses.insert(0,courses_2)
# # print(courses[0])
# # print(courses.extend(courses_2))
# # print(courses)
# # courses.remove('math')
# # print(courses)

# # courses.pop()
# # print(courses)

# # courses.reverse()
# # print(courses)

# # # courses.sort()
# # # print(courses)

# # nums=[1,3,4,6,67,3,2]
# # nums.sort()

# # print(nums)
# # print(nums.reverse())
# # # print(nums.sort(reverse=True))
# # # print(courses)
# # # courses.sort(reverse=True)
# # # print(courses)
# # # sorted(courses)
# # # print(courses)
# # print(min(nums))
# courses=['History',"Math","Physics","compSci"]
# print(courses)
# # print(courses.index("compSci"))
# # print(courses.index('Art'))
# # print('math' in courses)
# # print("art" in courses)
# for item in courses:
#     print(item)
# for course in courses:
#     print(course)
# for index,course in enumerate(course ,start=1):
#     print(index,course)
# course_str=", ".join(course)
# print(course_str)
# new_list=course_str.split("-")
# print(course_str)
list_1=["Histroy","Math","Physics","compSci"]
list_2=list_1
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)

#  immutable 
tuple_1=("Histry","Physics",'CompSci')
tuple_2=tuple_1

print(tuple_1)
print(tuple_2)
# tuple_1[0]='art'
print(tuple_1)
print(tuple_2)

#sets  
cs_courses={'Histry',"Math","Physics","CompSci",'mat'}
print(cs_courses)
art_courses={"Histroy",'Math',"Art","Design"}
print('math' in cs_courses)
print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))
print(cs_courses.intersection(art_courses))

# how to create a empty tuple and empty list and empty tuple 
empty_list=[]
empty_list=list()

empty_tuple=()
empty_tuple=tuple()

# empty_set={}this is nor an empty set this is the empty tuple 
empty_set=set()


























