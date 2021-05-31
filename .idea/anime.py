from bs4 import BeautifulSoup
import requests

uname=input("Enter username:")
source=requests.get("https://myanimelist.net/profile/"+uname).text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())

t1=soup.find('title').text
print(t1)

t2=soup.find('div',class_='stat-score di-t w100 pt8').text
print(t2)

print("Anime stats: ")
for t4 in soup.find_all('li',class_='clearfix mb12'):

   heading=t4.a.text+" "
   value=t4.span.text
   final=heading+value
   print(final)
   print(type(t4))

