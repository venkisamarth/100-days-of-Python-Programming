import random

# Generating random numbers 
# random() method 
# randint() method 
# randrange() method() method 
from random import randint
print(random.randint(0,100))
print(random.randint(1,6))
print("ranint() method in python ")
print(random.randint(10,100))
print(random.randint(12,99))

print("range() method in python")
print(random.randrange(1,100,2))

print(random.randint(10.0,200.0))
# python program to Generate 10 random numbers between 1-100
 
rand_nums=[]
for i in range(10): 
    rand_nums.append(random.randint(1,100))

print(rand_nums)

