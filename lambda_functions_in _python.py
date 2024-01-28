# A Function without name is called as lambda function 
# It is also as anonymous function 
# These function  are defined by using lambda keyword
#syntax 
#lambda arg_list:Expression

#How do we create the lambda funciont 
addition =lambda x,y: x+y

print("Result of addition:",addition(3,5))

# multiplication  function: 
multiplication=muliplication =lambda x,y:x*y
print("Result of multiplication:", multiplication(3,5))

# Square Function: 
square = lambda x: x**2 
print("Square of 5:",square(5))
# cube Function: 
cube =lambda x : x**3 
print("cube of 3:",cube(3))

# check Even number: 

check_even =lambda x: x%2==0
print(" Is 4 even?",check_even(4))


# string Reversal: 
reverse_string=lambda s: s[::-1]
print("Reversed string:",reverse_string("hello"))

# List Sorting : 
numbers=[3,1,4,1,5,9,2]
sorted_number=sorted(numbers,key=lambda x:x)
print("sprted number:",sorted_number)

#Filtering Even Number: 
numbers =[1,2,3,4,5,5,6,7,8,9,10]
even_numbers=list(filter(lambda x: x%2==0,numbers))
print("even numbers:",even_numbers)

# Maping squares 

numbers=[1,2,3,4,5]
square_numbers=list(map(lambda x:x**2,numbers))
print("squared numbers:",square_numbers)



