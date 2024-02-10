# How to read the content of the  file without using for loop 
f=open("hello.txt",mode="r")
for line in f: 
    print(line,end="")
f.close()

f=open("hello.txt",mode="r")
for line in f: 
    print(line,end=" ")

    