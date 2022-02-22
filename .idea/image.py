import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib
import json


url="https://api.jikan.moe/v3/search/anime?q=naruto"
json_obj=requests.get(url)
data=json.loads(json_obj.text)
print(data['results'])

