#opening file in python
# opening file 
# python provide an in built funciton open() to open a file 

# f=open("file name","r",'buffering',"encoding"=None,"error"=None,,"encoding"=None,"closefd"=True)
# f=open("filename","mode"="r")
# file =file to be accessed 
# mode =access mode (purpose of opening file )
# f=file handler .file pointer  

f=open("hello.txt")
if f: 
    print("file is opened")
print(type(f))

f=open("file path if the file in the other diractory.hello.txt")

if f :
    print("file is successfully opened ")
print(type(f))
