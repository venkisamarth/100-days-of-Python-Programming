# strip() 
# Removing leading and trailing characters from given staing 
# Three important inbuilt methods 
# # lstrip()
# strip()
# rstrip

# lstrip()
# it remove any leading character (space default leading character to remove)

# string lstrip(character) default space

# charcter - a set of  character  to remove as leading chracter It is optinal argument

# all combination of character of chracters are remove from left until first mistake

# lstip method on string 

# name=input("enter your name")
# print(name)
# name=name.lstrip()
# print(name)

url=["http://www.cricbuzz.com","http:www.youtube.com","http://www.facebook.com"]
for url in url:
    url=url.lstrip("htp:/w.")
    print(url)

# strip()
# It remove leading and traing character (space is the default character to remove)
# string strip (character)
# charcter - a set of charcter to remve It is optional argument

#  all combination of character are removed from left  first mismach then it remve right until
# first mismach
    
# url=["http://www.cricbuz.com","http://www.youtube.com","http://www.cricbuz.com"]
# for url in url:
#     url=url.strip("htp.com")
#     print(url)
url=['http://ww.cricbuz.com',"http://www.youtube.com","http://www.facebook.com"]
for url in url:
    url=url.rstrip("htp.com")
    print(url)

