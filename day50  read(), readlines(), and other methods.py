# f=open("example.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line,type(line))

# f = open("my_file2.txt", "r")
# i = 0

# while True:
#     i = i + 1
#     line = f.readline()

#     if not line:
#         break

#     m1 = int(line.split(",")[0])
#     m2 =int(line.split(",")[1])
#     m3 =int(line.split(",")[2])

#     print(f"Marks of student {i} in Maths is: {m1*2}")
#     print(f"Marks of student {i} in English is: {m2*2}")
#     print(f"Marks of student {i} in Python is: {m3*2}")

# f.close()

f=open("Myfile2.txt",'w')
lines=["line 1\n","line 2\n","line 3\n"]
f.writelines(lines)
f.close()

