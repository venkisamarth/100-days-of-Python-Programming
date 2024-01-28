#what is keyword argument
# provides key-value pairs as actual arguments 
# no need to mantain positions 
# number of parameter must be equal to no of arguments 
def info(name,age):
    print(f"name is {name} and the age is {age}")
info("jay",21)
info(name="venki",age=21)

# default arguments 
def info(name,age):
    print(f"name is{name} and age is {age}")
info(name="jay",age=21)

info(name="venki",age=12)

def info(name,age=50):
    print(f"name is {name} and the age is{age}")
info(name="jay")
info("veki")

# rules to adopt the keyword argumetns are  you canot give keyword argumts first
# personal inforamtion  printer 
#personal inforamtion printer
def print_info(name,age,country):
    print("Name:",name)
    print("Age:",age)
print_info(name="john",age=25,country="usa")
# Book Details Printer:
def print_book_details(title, author, year_published):
    print("Title:", title)
    print("Author:", author)
    print("Year Published:", year_published)

print_book_details(title="Harry Potter", author="J.K. Rowling", year_published=1997)
# Rectangle Area Calulation: 
def calculate_area(lenght,width): 
    return lenght * width
area=calculate_area(lenght=4,width=6)
print('Area of rectangle:',area)
#Circle Area Calculation 
import math 
def calculate_circle_area(radius):
    return math.pi*radius**2 
area=calculate_circle_area(radius=3)
print('Area of circle with readius 3:', area)

#Employee Inforamation 
def print_employee_info(name,id,departmet="Undefined"):
    print("Name:",name)
    print("ID",id)
    print("Department:",departmet)
print_employee_info('Alice',id=101)

# File Reader: 
def read_file(filename,mode="r"):
    with open(filename,mode)as file:
        return file.read()
content=read_file(filename="Example.txt")
print("content of file:",content)

#Email Sender: 
def send_email(to,subject,message,cc=None,bcc=None): 
    print("Email sent to:",to)
    print("Subject:",subject)
    print("Message:", message)
    if cc: 
        print("cc",cc)
    if bcc: 
        print("BCC:",bcc)

send_email(to="example@example.com", subject="Test Email", message="This is a test email.")
# Dictonary Merge: 
def merge_dict(dict1,dict2):
    merge_dict=dict1.copy()
    merge_dict.update(dict2)
    return merge_dict

dict1={"a":1,"b":2}
dict2={"c":3,"d":4}




