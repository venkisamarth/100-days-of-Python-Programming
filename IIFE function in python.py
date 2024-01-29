#IIFE (Immedialtely invoked function)
# result=(lambda num : num+1)(int(input("enter the number:")))
# print(result)

print((lambda x: print(x)(10)))
print((lambda x,y: print(x+y))(5,7))


result=(lambda x,y:x*y)(3,4)
print(result)

result=(lambda x: "even" if x%2==0 else "odd")(7)
print(result)

# IIFF with conditional logic 
    
result =(lambda x: "Even" if x%2==0 else "odd")(7)
print(result)

# IIFE with a list comprehension : 
sqaured =[(lambda x: x**2)(i) for i in range(1,5)]
print(sqaured)

# IIFF within another function : 
def outer_function(): 
    return (lambda x: x*2)(5)
print(outer_function())

#IIFE used in map function 
sqaured=list(map(lambda x: x**2,[1,2,3,4,5]))
print(sqaured)

# IIFE  used in map 
sqaured=list(map(lambda x: x**2,[1,2,3,4]))
print(sqaured)

#IIFE with a default parameter
result =(lambda x=5: x*2)()
print(result)

#IIFE with a default parameter
result =(lambda x=5: x*2)()
print(result)
#IIFE with unpaking
result =(lambda * args: sum(args))(1,2,3,4)
print(result)

result =(lambda x:(lambda y:x+y)(5))(10)
print(result)







