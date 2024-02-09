# File object methods : 
# readble()
# writable()

f=open("hello.txt",mode="r")
print(f.readable())
print(f.writable())
f.close()


f=open("hello.txt",mode='w')
print(f.readable())
print(f.writable())
f.close()

f=open("hello.txt",mode='r')
if f.readable(): 
    print("file is readble")
f.close()


