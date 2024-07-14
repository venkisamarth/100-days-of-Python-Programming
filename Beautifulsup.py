# import requests
# from bs4 import  BeautifulSoup
# url ="https://www.wscubetech.com/"
# r=requests.get(url)

# print(r.text)
# soup=BeautifulSoup(r.text,"lxml")
# print(soup)
import requests 
from bs4 import  BeautifulSoup
url="http://webscraper.io/test-sites/e-commerce/allinone/computers"
r=requests.get(url)


# print(r.text)
soup =BeautifulSoup(r.text,"lxml")
# print(soup)
print(soup.div)






