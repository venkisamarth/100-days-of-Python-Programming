# -*- coding: utf-8 -*-
"""Day23 list methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RkM4qR9GXSv4uNhPcMq8LzHzc3tArDz3

append():
"""

my_list=[1,2,3,4]
my_list.append(4)

print(my_list)

another_list=[1,2,3,4,5,6]
another_list.append("c")
print(another_list)

"""extend(iterable):"""

my_list=[1,2,3,4]
my_list.extend([4,5])
print(my_list)

another_list=["a","b"]
another_list.extend(["c","d"])
print(another_list)

"""insert():"""

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)

another_list=["a","b","c"]
another_list.insert(2,"f")
print(another_list)

"""remove(x)"""

my_list=[1,2,3,4,5,6]
my_list.remove(2)
print(my_list)

another_list=["a","b","c","d"]
another_list.remove("b")
print(another_list)

"""pop()"""

my_list=[1,2,3,4,5]
popped_element=my_list.pop(2)
print(popped_element)
print(my_list)

"""index(x[,start[,end]]):"""

my_list=[1,2,3,4,5]
index=my_list.index(3)
print(index)

another_list=["a","b","c","b"]
index=another_list.index("b",1)
print(index)

"""counts(x):"""

my_list=[1,2,3,4,5,6]
count=my_list.count(2)
print(count)

anothe_list=["a","b","c","b"]
count=another_list.count("b")
print(count)

"""sort(key=None,reverse=False):"""

my_list=[3,4,5,6,4,56]
my_list.sort()
print(my_list)

another_list=["apple","bababa","orange"]
another_list.sort(reverse=True)
print(another_list)

"""reverse():"""

my_list=[1,2,3,4,5]
my_list.reverse()
print(my_list)

another_list=["a","b","c"]
another_list.reverse()
print(another_list)

"""copy():"""

original_list=[1,2,3]
copied_list=original_list.copy()
print(copied_list)

another_original_list=["x","y","z"]
another_copied_list=another_original_list.copy()
print(another_copied_list)

