# what is frozenset?
#frozenset is immutable version of python set 
#while elements of a set can be modified  at any time,elements of the frozen set remain the same after creation 
# how to create forzenset?
#  syntax : forzenset(iterable)

#Note if we dont pass any iterable it should be empty  forzen 


## how forzenset is differ from the normal set 
#there are no method like set update, remove, for forzensetlike set frozen===unchangelble
vowels={"a","e","i","o","u"}
fset=frozenset(vowels)
print(fset)
print(type(fset))
# creating the forzenset using the list 
vowels=["a","e","i","o","u"]
fset1=frozenset(vowels)
print(fset1)
print(type(fset1))
#creating the forzenset using dictionary
d={"one":1,"two":2}
fset3=frozenset(d)
print(fset3)
print(type(fset3))
# creating the forzen set using stirng 
vowels='aeiou'
fset4=frozenset(vowels)
print(fset4)
print(type(fset4))

fset={'a',"e","i","o","u"}
fset2=frozenset(fset)
print(type(fset2))
print(fset2)
print(fset.union(fset))
print(fset.intersection(fset2))
print(fset.symmetric_difference(fset2))
print(fset.difference(fset2))
print(fset.issubset(fset2))
print(fset.pop())
print(fset)

fset.add('w')
print(fset)




print(type({})is set )

nums=set([11,11,22,22,33,33,44,44])
print(len(nums))
#print(({1,2,3}+{4,5,6}))
#error

empty_set=set()
print(type(empty_set))
print(empty_set)

set1={10,20,30,40}
set2={50,20,10,60}
set3=set1.union(set2)
print(set3)

sampleset={'yellow',"orange",'black'}
sampleset.discard("blue")
print(sampleset)


# sampleset=["yellow","orange","black"]
# sampleset.update(["blue","gree","red"])
# print(sampleset)

# sampleset={"yellow","orang","black"}
# print(sampleset[1])

set1={10,20,30,40,50}
set2={60,70,80,90,20,50}
print(set1.issubset(set2))
print(set2 .issubset(set1))
print(set2.issuperset(set2))

sampleset={"yello","ornage","Black"}
sampleset.add("Blue")
sampleset.add("orange")
print(sampleset)

s={"123","coyug",(1,2,3),2+3j}
print(s)

set1={1,2,3}
set2={4,5,6}
print(len(set1.union(set2)))







