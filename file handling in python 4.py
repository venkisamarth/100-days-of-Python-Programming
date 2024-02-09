# open function argments/file handling buffering  

# f=open(filename,mode="r",buffering,encoding=None,error=None,newline=None,closefd=True)
# buffering 
#positive Interger value used to set buffer size of for file 

# In text mode ,buffer,size,should, be 1 or more than 
#Default In binary mode buffer size can be 0 


# Encoding type used to decode and encode file 
# should be used in text mode only 
# defalut value depend on os 
# for windows =cp12345
 

#error Repersents how enocoding and decoding errors are to be handled 
# cannot be used in binary mode 
# # some standard values are : strict ignore replace etc 
#  newline 
# It can  be 
f=open("hello.txt",mode="r",buffering=10,encoding="utf-8" )
if f: 
    print("opend")
print(f)

f=(open("hello.txt",mode="r",buffering=10))
if f: 
    print("opend")
print(f)

# f=open("hello.txt","r","utf-8")
# if f: 
#     print(f)






