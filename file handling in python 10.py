# mode of openig file :
f=open("mytext.txt",mode="r")
data=f.read()
print(data)
f.close()

f=open("mytext.txt",mode="rb")
data1=f.read()
print(data1)
f.close()