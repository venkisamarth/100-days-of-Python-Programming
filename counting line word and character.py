f=open("hello.txt",mode="r")
number_of_words=0 
number_of_chars=0 
number_of_lines=0 
for line in f: 
    number_of_lines +=1 
    line=line.strip("\n")
    number_of_chars+=len(line)
    list1=line.split()
    number_of_words+=len(list1)

f.close()
print("number of lines:",number_of_lines)
print("number of words",number_of_words)
print("number of character",number_of_chars)