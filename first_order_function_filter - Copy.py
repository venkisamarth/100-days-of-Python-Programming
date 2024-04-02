numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

# fitler names string with 'j' from a list : 
names =['John',"jane","Doe","jack","jill"]
j_names=list(filter(lambda name:name.startswith('J'),names))
print(j_names)
#Filter positive numbers from a list : 
numbers =[-3,-2,-1,0,1,2,3]
positive_numbers=list(filter(lambda x:x>0,numbers))
print(positive_numbers)

# Filter strinng with lenght greter than 3 from  a list 
string =["apple","banana","cat","dog","elephant"]
long_string=list(filter(lambda s: len(s)>3,string))
print(long_string)

# Filter prime numbers from a list : 
def is_prime(n): 
    if n<=1: 
        return False
    for i in range(2,int(n**0.5) +1): 
        if n %i ==0: 
            return False
    return True
numbers =range(1,20)
prime_numbers=list(filter(is_prime,numbers))

# fitler uppercase letter from a string 
sentence ="hello world! How are you"
uppercase_letters=list (filter(str.uppercase,sentence))
print(uppercase_letters)
# Filter even-lenght strings from a list : 
strings = ["one", "two", "three", "four", "five", "six"]
even_length_strings = list(filter(lambda s: len(s) % 2 == 0, strings))
print(even_length_strings)  # Output: ['two', 'four']
 




