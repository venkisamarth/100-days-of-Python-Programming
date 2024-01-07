

# # try:
# #     # Open the file
# #     with open("my_file.txt", "r") as f:
# #         print(f)  # Print file object information

# #         # Read the content of the file
# #         text = f.read()
# #         print("File Content:")
# #         print(text)
# # except FileNotFoundError:
# #     print("Error: File not found.")
# # except PermissionError:
# #     print("Error: Permission denied to read the file.")
# # except Exception as e:
# #     print(f"An unexpected error occurred: {e}")
# # # reading the file 
# # g=open("my_file2.txt","r")
# # text=g.read()
# # print(text)
# # # writing to the file 
# # new=open("my_writingfile.txt","a")
# # f.write("Hello,  this is the python world this  world is  butiful world")
# # text=new.read()
# # print(text)
# # new.close()
# f=open("my_file.txt","a")
# f.write("hello, world!")
# with  open("my_file.txt","a")as f:
#     f.write("Hey I am insdie with")
#opening the file with the read mode 
with open("example.txt","w") as file:
    content=file.read()
    print(content)

# "w" Write Mode:
# open the file for writing
# if the file does't exist it create a new file
# if the file already exists , it truncates the file to zero lenght
with open("new_file.txt","w")as file:
    file.write("Hello, this is new file!")
    




