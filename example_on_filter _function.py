# laptops={"hp":50000,"lenovo":60000,"macbook":120000}
# budget=float(input("enter your budget: "))
# def fitler_items(ele):
#     if laptops[ele]<=budget: 
#         return True
#     else: 
#         return False 
# filter_object= list (filter(fitler_items,laptops))
# print(filter_object)
# for ele in filter_object:
#     print(ele) 

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

# Fitler odd numbers: 
numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)

#filter  positive numbers 
numbers =[-2,-1,0,1,2,3,4,5]
positive_numbers=list(filter(lambda x: x>0,numbers))
print(positive_numbers)

#filter negative numbres: 
numbers=[-2,-1,0,-1,2,3,4,5]
negative_numbers=list(filter(lambda x: x<0,numbers))
print(negative_numbers)

# fitler strings longer than 5 character 
words =["apple","banana"," orange","kiwi","strawberry"]
long_words=list(filter(lambda x:len(x)>5,words))
print(long_words)

#fitler  names string with "A"
names=["Alice",'venki',"Anna","Alex","David"]
a_names=list(filter(lambda x: x.startswith("A"),names))
print(a_names)

# Filter prime numbers: 
def is_prime(n): 
    if n<=1: 
        return False
    for i in range(2 ,int(n**0.5)+1): 
        if n %i==0: 
            return False
    return True
numbers=[2,3,4,5,5,6,6,10,30]
prime_numbers=list(filter(is_prime,numbers))
print(prime_numbers)

#fitler elments divided by 3 and 5: 
numbers = [15, 20, 25, 30, 35, 40, 45, 50]
divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(divisible_by_3_and_5)

#filtre flots: 
mixed_data=[1,2.5,"a",3.7,'b',4,5.2]
floats=list(filter(lambda x:isinstance(x,float),mixed_data))
print(floats)


