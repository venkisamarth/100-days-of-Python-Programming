# f=open("hello.txt")
# #operation  
# f.close()
# check file exist or not: 
# is file()

#This method i used to check file exist or not  
#this  method belongs to path module which is sub_modele of as model 

# syntax 

# import os 
# print(os.path.file("hello.txt"))

# import os  
# if os.path.isfile("hello.txt"):
#     f=open("hello.txt")
#     f.close()

# else: 
#     print("file not exist")

import os  
filename=input("Enter the file name")
if os.path.isfile(filename): 
    f=open("filename")
    f.close()
else: 
    print("file not exist")

    