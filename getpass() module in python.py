#The getpass is a module in python 
#It asks the user for a password without enchosing  which means whithout  displaying what the user is typing 
# suported only for terimanal_based apps 

# import getpass
# my_pass=getpass.getpass(prompt="Enter the password")
# if my_pass=="admin": 
#     print("login succesfully")
# else: 
#     print("login failed,incorrenct password")
# getuser()
    
import getpass
user_name=getpass.getuser()
print(user_name)
pass_word="admin"
#interface
user=input("Enter the  username")
pass_word=getpass.getpass()
if user==user_name and pass_word==pass_word: 
    print("do operations")
else: 
    print("incorrect credentials")
