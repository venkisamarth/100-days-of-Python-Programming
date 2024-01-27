# return is also statment
# return is also one of th keyword 

p=10000
n=3 
r=12.25

def simple_interest(p,n,r):
    si=(p*n*r)/100
    print("simple interest is:",si)
    return si 
# simple_interest(p,n,r)

si=simple_interest(p,n,r)
print(si)
total_pay=p+si
print("The totle payable amount is :", total_pay)

# you can return the multiple values 

def add(a,b):
    sum1=a+b
    sum=a-b
    return sum1,sum
sum,sub=add(1,2)
print(sum)
print(sub)





