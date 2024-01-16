# what is set and how to create set 
# charaterstircs of set 

# a  set is an unorderd collection of iterms of diffrence types encolsed types in curly breacekets

# example =
# Two ways 
#  1) using curly braces 
# 2) using set() fucnion 



# first ways of creating set 
s={"hello",101,10.3, 2+3j} 
print(type(s))
print(s)

# Importance of sets 
# example 
s={10,20,10,10,20,20,30,40}
print(s)

# no duplicants ara allowed  isidethe set 
# elements are not in particuler order 
s={10,20,30,40,50}
print(s)
# indexing and slicing  cannot be application on set 
s={10,20,30,40,50}
# print(s[1])

# 4 set is immutable  
s={10,20,30,40,50,60}
s.add(100)
print(s)

# 100 will be added at any possition of the  set 
s={10,10,20,30,40}

s.add(100)
print(s)
# element in set must be immutable 
s={10,20,10,10,(10,20,30,40,50)}
print(s)

#creating empty set:
empty_set=set()
print(type(empty_set))
# set with single element  
print(type(s))
v={23,}
print(type(v))





