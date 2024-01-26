#simple if Statement:
x=10 
if x>5:
    print("x is greter thean 5")

# if else Statement
x=10 
if x%2==0:
   print("x is even number ")
else:
    print("x is the even number ")


# Nested if Statement 

x=10 
if x>5:
    if x<15:
        print("is between 5 and 15")

# Multiple Elif Statments 
x=7
if x==5:
    print('x is 5')
elif x==7:
    print('x is 7')
elif x==10:
    print("x is 10")
else:
    print("x is not 5, 7, or 10 ")

# if elif else:

x=10 
if x>0:
    print(" x is possitive ")
elif x<0:
    print('x is negative')
else:
    print('x is Zero')

# if statments with logical operateres 

x=10 
if x>5 and x<15:
    print(" x is between 5 and 15")

my_list=[1,2,3,4,5]
x=6 
if x in my_list:
    print(" x is in the list")
else:
    print(" x is not in the list")
# if statment with identity operaters 

x=[1,2,3]
y=[1,2,3]
if x is y:
    print("x and y are the same object")
else:
    print(" x and y are diffrent objects")

# if statments with Truthiness
x=10 
if x:
    print('x is true')
else:
    print('x is false')


    



