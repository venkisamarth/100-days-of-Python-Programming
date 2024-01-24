# comprehension is a concis way to create a list 
# in python it allows you to create a new list applyinng an expression to eacj item inan existing iterable and 
# optionally filtering the items based on a condition  

# basic squares:
squares=[x**2 for x in range(5)]
print(squares)

# souble each elements in list 
numbers =[1,2,3,4,5]
double =[x*2 for x in numbers ]

print(double)
# double each elements in the list 
numbers =[1,2,3,4,5,67,8,9,10]
evens =[x for x in numbers if x%2==0]
print(evens)

# Filter even numbers:
numbers =[1,2,3,4,5,6,6,6]
evens =[x for x in numbers if x%2==0]
print(evens)
# List to tupls
pairs=[(x,x*2) for x in range(4)]
print(pairs)

# String manuputlation 
words = ['hello', 'world']
upper_case = [word.upper() for word in words]

# Flatten a 2D
matrix =[[1,2,3,4,5],[4,5,6],[7,8,9]]
flattend =[num for row in matrix for num in row]
print(flattend)

# Filter and transform
numbers=[1,2,3,4,5,6,7,8,9,10]
filterd_squared=[x**2 for x in numbers if x%2 ==0]
print(filterd_squared)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squared_nested = [[x**2 for x in row] for row in nested]
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# conditional ternary expression
numbers =[1,2,3,4,5]
result=['even' if x%2==0 else 'odd' for x in numbers]
print(result)

sentence = "Hello World"
vowels = [char for char in sentence if char.lower() in 'aeiou']
# Output: ['e', 'o', 'o', 'o']
print('**'*5)
lst=[]
for i in range(1,4):
    for j in range(5,7):
        lst.append(i+j)
print(lst)

print([i*j for j in range(5,7) for i in range(1,4)])
print("list comprehension with if condition")

numbers=[1,2,3,4,5,5,6,7,8,9,10]
evens=[x for x in numbers if x %2==0]

# Filter positive numbers
nums=[-2,-1,0,1,2,]
positive=[x for x in nums if x>0]
print(positive)

# Remove vowels from a string 

sentace ='Hello world'
consonents =[char for char in sentace if char.lower() not in 'aeiou' ]
print(consonents)

# selected uppercase letters:

mixed_case = "HeLLo WoRLd"
uppercase_letters = [char for char in mixed_case if char.isupper()]
print(upper_case)
# Output: ['H', 'L', 'L', 'W', 'R', 'L']
# Selectd uppercase letters:
mixed_case='Hello WoRLd'
uppercase_letters=[char for char in mixed_case if  char.isupper()]
print(mixed_case)






