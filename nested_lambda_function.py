# def Display(msg): 
#     def screen(): 
#         print(msg) 
# # nested lambda function 
# add=lambda x: lambda y:x+y
# print(add(10))


nested_lambda_1=lambda x: lambda y:lambda z: x+y+z
result_1 =nested_lambda_1(1)(2)(3)
print(result_1)

# example 2 
nested_lambda_2 =lambda a: lambda b:lambda c: lambda d:lambda c : lambda e: lambda f: a*b * c* d* e* f
result_2=nested_lambda_2(1)(2)(3)(4)(5)(6)
print(nested_lambda_2)

nested_lambda_2 = lambda a: lambda b: lambda c: lambda d: lambda e: lambda f: a * b * c * d * e * f
result_2 = nested_lambda_2(1)(2)(3)(4)(5)(6)
print("Example 2 Output:", result_2)
# example 4 
nested_lambda_4 =lambda a: lambda b:lambda c: lambda c: lambda d: lambda e:lambda f : a+b-c*d/e+f
result_4 =nested_lambda_4(10)(5)(3)(2)(4)(7)
print("Example 4 output:", result_4)

# example 5 
nested_lambda_5=lambda x: lambda y: lambda z: x**(y+z)
result_5 =nested_lambda_5(2)(3)(4)
print("example 5 outPut:",result_5)

nested_lambda_6 =lambda a: lambda b: lambda c: lambda d: lambda e: lambda f: lambda g:a*b+c-d/e*f/g 
result_6=nested_lambda_6(10)(2)(5)(4)(2)(2)(5)
print("example 6 output:",result_6)

nested_lambda_8 = lambda a: lambda b: lambda c: lambda d: lambda e: lambda f: lambda g: lambda h: a * b / c + d ** e - f * g + h
result_8 = nested_lambda_8(4)(2)(3)(1)(2)(5)(3)
print("Example 8 Output:", result_8)