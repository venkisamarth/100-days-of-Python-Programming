 
# closing  file : 
# How to close a file 
# what is used of closing  file 
# what is used closing file 
# what happens if we do not close a file 
# after  performig  operation , we  have to close a file 

# close(): function used to close  a file  

# syntax 

# file_handle_close()

#what happens when we close a file :
#file object is deleted form memorey and file is no more accessible from memory and file is no more accessible u=unless we open it again 
# what happen when we do not colose a file  
#after program excecution pytho garbage collector grabage collector will destroy file object and closes file autometically 
# possible  outcomes 
# data will corrupt  
# memory watstage 
f=open("hello.txt","r")
if f: 
    print("file is opened in  ready for the work")
f.close()

