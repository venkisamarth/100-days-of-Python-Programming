# seek() and tell() functions
# In Python, the seek() and tell() functions 
# are used to work with file objects and 
# their positions within a file. These functions are
# part of the built-in io module, which provides a consistent
# interface for reading and writing to various file-like objects,
#  such as files, pipes, and in-memory buffers.



# seek() function

#The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you 
#can move either forward or backward from the current position. For example:
# with open('file.txt', 'r') as f:
#   # Move to the 10th byte in the file
#     f.seek(10)
#   # Read the next 5 bytes
# data = f.read(5)
    
# with open('example.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(0)

#   # Read the next 5 bytes
#   data = f.read(5)
#   print(data)

  #tell() fucniton
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position
# relative to the current position. For example:
# with open("example.txt",'r') as f:
#   data=f.read(10)
#   current_position=f.tell()
#   f.seek(current_position)
#   print(data)

# truncate() fucniton
# when you open a file in Python using the open fucnion, you can specify the 
# mode in which you want  to open the file. If you specify the mode as 'w'
# or 'a' the file is opend in write mode and you can write to the file. However
#  if you want to truncate  the file to a specificsize, you can use the truncate  function.function
# here is an example of how to use the truncate  function:

# with open('my_file2.txt','w')as f:
#   f.write("Hello World!")
#   f.truncate(6)
  
# with open("sample.txt",'r') as f:
#   data=f.read()
#   print(data)

# with open("example.txt",'w') as f:
#   f.write("Hello, World!")
#   data=f.read()
#   print(data)

with open('sample.txt', 'w') as f:
  f.write('Hello World!  this is the more clear this ')
  f.truncate(111)

with open('sample.txt', 'r') as f:
  print(f.read())

  

