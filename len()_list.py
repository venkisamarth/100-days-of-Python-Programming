# lenght of the list using the len() function 
l1=[12,13,14,15,16,17,18,19]
print(len(l1))
print("**"*3)
print("the lenght of the list is:",len(l1))
print("$$"*23)
# by writing manula program 
count =0
for element in l1:
    count =count+1 # or count +=1
print(count)

#write a program that couts the numbers of character in a given string 
inupt_string="hello world!"
count=0
while count<len(inupt_string):
    count +=1
print(f'the number of cahraacter in the string is:{count}')
# revers a string usig hte string 
input_str="python"
reversed_string=""
index=len(input_str)
while index>=0:
    reversed_string=reversed_string+input_str[index]
    index-=1
print(f"The rverse string is:{reversed_string}")

# counts the number of vowels in stirng 
input_str="hello world"
vowels="aeiouAEIOU"
count=0
index=0
while index <len(input_str):
    if input_str[index] in vowels:
        count =count +1
    index+=1
print(f"The number of vowels in the string is:{count}")
