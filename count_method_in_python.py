# how to count number of occurence of the specific substring in string
# how to see index of that string
# count()

# 3 inbuilt method returns a number of times a specified substring occurence of times 
# a specified substring occurence in a string 
# # sysntax 
# string.count (substring,start,end)

# substring -A string whose occurence is to be calculated 

# start- from where to start searching (end index)
# end where to end searching (end index)
# importent 
# start =optional
# # end =optional

str=input('enter the string')
counter= str.count('v')
print(counter)
str1=input("enter the string")
counter=str1.count("O",3,6)
print(counter)







