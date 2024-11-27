if False:
    print('conditional was True')
 
language ='java'
if language=='python':
    print('lanaguage is not a python')
elif language=='java':
    print("Language is Java")
elif language=="javascript":
    print("javascritp")
else:
    print('No match')
user="Admin"
logged_in=True
if user==logged_in and "Admin":
    print('Admin Page')
else:
    print('Bad Creds')


user="Admin"
logged_in=False
if not logged_in:
    print("please log In")
else:
    print("Welcome")

if not logged_in:
    print('please log In')
else:
    print('welcome')

a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)

print(id(a))
print(id(b))
print(a is b)

print(id(a)== id(b))

condition=False
if condition:
    print("Evaluate to True")
else:
    print('Evaluate to false')








