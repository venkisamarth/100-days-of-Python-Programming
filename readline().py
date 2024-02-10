#the function is used to read a single line form a file 
# syntax 
# file_object.readline(size)
f=open("hello.txt",mode="r")
data1=f.readline()
print(data1)
data2=f.readline()
print(data2)
data=f.readline(10)
print(data)
f.close()
#data=f.readline()
#print(data)

      
