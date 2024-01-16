
# 3 union of sets 
# 4 intersection of sets
# 5 diffrence of sets 
# 6 symmetric diffrence 
# 7 comparing sets

# what is the union of two sets 
##union of two sets is deffined as the smallest sets which contaions all the elements of 
#both the sets

# example 
# example 
a={2,3,4,5,6}
b={4,5,6,7,7} 
print(a.union(b)) 

# union in python set 
# by using operator(1)

# syntax union() set1!set2

print(a|b)

# by using the union function 
s1={10,20,30,40,50}
s2={20,40,50,60,80}
print(s1|s2)

# what is the intersection of two sets 

# intersection of two sets is the largeset set which contains all elements that are comman to both the sets 
# example 

# by using intersection operatere (&)


set_1={1,2,3,4,5,6}
set_2={12,3,3,4,5}
set_3=set_1.intersection(set_2)
print(set_3)

# using the symbole of the & operatere
print(set_1&set_2)

#diffrence and symmetric diffrence of two sets 


#diffrence sets = the diffrence between two sets in python is equal to the diffrence between the numbmer of element
a={2,4,5,6}
b={4,5,7,8}
print(a-b)
print(b-a)

# diffrence of python sets 

# by using sunstaraction operator 
# syntax =set_name1.diffrence(set_name2)


# by using diffrence () function (setname2)

a={2,4,5,6,7}
b={4,5,6,7}
print(a.difference(b))
print(b.difference(a))

# symmetric is symmetric diffrence between two sets?
# the symmetric difference of two sets is a set of elements
#  that are in either sets but ot in there intersection 

# example 

a={2,4,5,6}
b={4,5,6,7}
print(a^b)
print(b^a)

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
s1={10,20,30,40,50}
s2={20,40}
s3={20,40}

print(s1)
print(s2)
print(s3)








