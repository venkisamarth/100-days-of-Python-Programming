def sum1(num1,num2,num3):
    return num1+num2+num3
result=sum1(10,20,30)
print(result)

# Varaible lenght keyword arguments 
def sum_numbers(*args):
    return sum(args)
result =sum_numbers(1,2,3,4,5)
print("sum of numbers :",result)

#Concatination of strings: 
def concatenate_strings(*args):
    return ''.join(args)

result = concatenate_strings("Hello", ", ", "world", "!")
print("Concatenated string:", result)
# Avarage Calculation : 
def calculation_avarage(*arags): 
    return sum(arags)/len(arags)

average=calculation_avarage(10,20,30,30,40,50)
print("Avarage:",average)
# mximum number of Find 
def find_max(*args): 
    return max(args)
maximum=find_max(10,20,30,20)
print("Maximum number:",maximum)
# minimum number finder: 
def find_minimum(*args): 
    return min(args)
mimimum=find_minimum(10,20,30,40)
print("minmum number:",mimimum)

# miltiple of numbers 
def multiple_numbers(*args):
    result=1
    for num in args: 
        result *=num
    return result
result=multiple_numbers(2,3,4)
print("Restul of multiplication: ",result)

# List Printer
def print_list(*args): 
    for items in args: 
        print(items)
print_list(1,'a',True,[2,3,4])

#Even numbers Filter: 
def filter_even_number(*args): 
    return[num for num in args if num % 2 ==0]

even_numbers=filter_even_number(1,2,3,4,5,6)
print("Even numbers:",even_numbers)

# Square of numbers: 
def reverse_strings(*args):
    return [string[::-1] for string in args]

reversed_strings = reverse_strings("apple", "banana", "orange")
print("Reversed strings:", reversed_strings)
# reverse sttring 
def reverse_string(*args): 
    return [string[::-1] for string in args]

reverse_string=reverse_string("apple","banana","orange")
print("Reversed string:",reversed_strings)












