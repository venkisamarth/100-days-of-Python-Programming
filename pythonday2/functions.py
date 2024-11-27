def hello_func():
    print("Hello Function.")
print(hello_func())
hello_func()
hello_func()
hello_func()
hello_func()
def name():
    return 'venkates'
print(name().upper())
print(name().upper())
print(name().upper())

def hello_function(greeting):
    return "{} fucntion.".format(greeting)

print(hello_function('this is the '))

def hello_functio(greeting,name="venkatesh"):
    return '{},{}.'.format(greeting,name)
print(hello_functio('hyyy'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Math',"art",name="jayapppa",age=24)
def student_inf(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['math','compsci']
info={"name":"venki","age":23}
student_inf(*courses,**info)

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    # Doc String in python  is the give the explaination about the code 
    """Return True for leap year, False for non-leap year."""
    return year % 4 and (year %100 !=0 and year %400==0)
def days_in_month(year,month):
    "Returns number of days in that months in that year "
    if not 1<=month<=12:
        return "Invalid Month"
    if month==2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2017))
print(is_leap(2020))
print(days_in_month(2017,2))

