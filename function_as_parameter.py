# A function is an object 
# we can create alias for the function 

# function as object 
#Higher-order Function for claculation : 
def calculate(operation,x,y): 
    return operation(x,y)

def calculate(operation, x, y):
    return operation(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

restul_add=calculate(add,5,3)
restul_subtract=calculate(subtract,8,2)
print("Addition result:",restul_add)
print("Subtract result:",restul_subtract)  

# filtering with Custom Criteria
def filter_elements(Criteria,elements):
    return [elements for elements in elements if Criteria(elements)]

def is_even(number): 
    return number%2==2
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=filter_elements(is_even,numbers)
print("Even numbers:",even_numbers)

#callback for Asynchornous operations: 
def async_operation(callback):
    # Simulating an asynchronous operation
    result = "Data from async operation"
    callback(result)

def handle_result(data):
    print("Handling result:", data)

async_operation(handle_result)

# Sorting with coustom Comparater: 
def custom_sort(elements,key): 
    return sorted(elements,key=key)
def sort_key(element): 
    return len(element)
word=['apple','banana',"orange","kiwi"]
sorted_words=custom_sort(word,key=sort_key)
print("Sorted words by length:",sorted_words)



