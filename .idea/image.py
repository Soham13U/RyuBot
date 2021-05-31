import requests
from bs4 import BeautifulSoup
import urllib.request


source=requests.get("https://myanimelist.net/profile/Xoham").text
soup=BeautifulSoup(source,'lxml')
images=soup.find_all("img")
i=0
for image in images:
    if i == 2:
        break
    else:
        href=image.get('data-src')

    i=i+1

print(href)