# iteration through the  string 
name ="shanthanu"
for char in name :
    print(char,end=",")

# find lenght of the string 
# lenght os the string is nothing but number of char in the particuler string 
# Two ways to finding of lenght 
# 1) by manual programing 
# 2) by len() function
    
# this is the manual method 
# str1=input("enter the string")
# count=0
# for char in str1:
#     count =count+1
# print(count)
# # this is uisin the inbuilt funtion
# name=input("enter your name: ")
# print(len(name))
    
#string membership 
    
name="codeyug"
if "co" in name:
    print('present')
# how to calculate ovwels in the string 
str1=input("enter the any string")
vowel=["a","e","i","o",'u']
count=0
for char in str1:
    if char in vowel:
        print(count)





