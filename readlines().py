# this is used to read all lines from a file and  reaturn a list  off  lines  
#syntax file_object.readlines()
f=open("hello.txt",mode="r")
data=f.readlines()
print(data)
f.close()
# It  gives the all lines()
# It  gives the all lines in th form of lines 
f=open("hello.txt",mode="r")
data=f.readlines()
for line in data: 
    print(line,end="")
f.close()