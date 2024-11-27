# # import my_module as mm
# from my_module import *
# from my_module import find_index, test
# import sys
# # sys.path.append("")
# import sys 
# courses =["History","Math","Physics","ComSci"]
# index =find_index(courses,"Math")
# # index = mm.find_index(courses,"Math")
# # print(index)
# # print(test)
# print(sys.path)
import random
courses=["Histry","Math","Physics","ComSci"]
random_courses=random.choice(courses)
print(random_courses)

import math 
rads =math.radians(90)
print(rads)
print(math.sin(rads))


import datetime
import calendar
today= datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os 
courses=["Histroy","math","Physics","CompSci"]
print(os.getcwd())
print(os.__file__)


# import antigravity


