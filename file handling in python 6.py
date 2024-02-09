# File object varaibles in python 
# name =has name of specified file 
# mode =mode of specified  file 
# closed =has boolean valu shows  
# file closed or not 

# Encoding= has encoding  name 


# syntax =file-object.varaible_name

# f=open("mytext.txt",mode="r",encoding="utf-8")
# print(f.name)
# print('file name is :',f.name)

f=open("abifile.txt",mode="r")
if f: 
    print("file is opened it is ready for work")
f.close()
f=open("abifile.txt","r")

print("encoding is:",f.encoding)
print("mode is:",f.mode)
print("if file is closed?",f.closed)
f.close()
print(f.closed)


