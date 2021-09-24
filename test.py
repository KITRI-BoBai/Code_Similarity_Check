import requests
import re
from bs4 import BeautifulSoup


url = 'http://192.168.128.142:9000/'
data = {'code' : 'test'}

response = requests.post(url,data=data)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
similarity = str(soup.find_all('h1')[2])
similarity=re.sub('<.+?>', '', similarity, 0).strip()
print(similarity)

