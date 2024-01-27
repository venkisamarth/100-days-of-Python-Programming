# Varaible delclared ouside function are called as globle varaible
b=2000
def Demo():
    a=100
    print(a)
a=500
print(a)
Demo()

def Demo(c):
    b=100
    sum1=b+c
    print(sum1)

Demo(200)
print(a)

def Display():
    print(a)


a=10 
def Demo():
    b=a+5 
    print(b)
a=10 
def Demo():
    a=a+5 
    print(b)
Demo()


