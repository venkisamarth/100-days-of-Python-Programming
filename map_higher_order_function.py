#This is the built in higher order function it apply a specific 
#function on each elements of the iterable  and perhaps changes elements


# program for finding square of each numbers 

nums=[3,4,4,6]
def square(n): 
    return n*n
maped=map(square,nums)
print(maped)
print(type(maped))

for ele in maped: 
    print(ele)
print(list(maped))

#square each elements in list 
numbers =[1,2,3,4,5,6,6]
squared_numbers=list(map(lambda x: x**2,numbers))
print(squared_numbers)
convert =['apple',"banna","orange","kiwi"]
uppercase_words=list(map(str.upper,convert))
print(uppercase_words)
# get the lenght of the strings in a list 
word=['apple',"banana","orange","kiwi"]
word_lenghts=list(map(len,word))
print(word_lenghts)
#Get the lenghts of strings in list 
words=['apple',"banana","orange","kiwi"]
word_lenghts=list(map(len,words))
print(word_lenghts)
#calculate the square roots os each numbers in  list 
import math
numbers=[1,2,3,4,5,6]
sqrt_numbers=list(map(math.sqrt,numbers))
print(sqrt_numbers)
# convert a list of integers to their binary representaion 
numbers=[10,20,30,40,50]
binary_numbers=list(map(lambda x: bin(x)[2:],numbers))
print(binary_numbers)

#sqrt_numbers=['10','20','30','40','50']
int_numbers=list(map(int,sqrt_numbers))
print(int_numbers)

# convert list of tupls to list of their sum 
tuples =[(1,3),(3,4),(5,6)]
sums = list(map(lambda x: x[0] + x[1], tuples))
print(sums)

#Flatten a list of lists: 
nested_list=[[1,2,3,],[4,5,6],[7,8,9]]
flattened_list=list(map(lambda sublist: sublist,nested_list))
print(flattened_list)

# multiply corresponding elements of two lists: 
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
result=list(map(lambda x,y:x*y,list1,list2))
print(result)