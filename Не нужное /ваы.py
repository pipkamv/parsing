import lxml
import requests
from bs4 import BeautifulSoup
import json


debug = 'https://app.inventorysource.com/views/supplier/index.html'
session = requests.Session()
auth = session.post('https://app.inventorysource.com/#/login', data={'login':'aruslan@rubekstore.com','password':'almaty1999'})
res = session.get(debug)
soup = BeautifulSoup(res.content)
element = soup.find('div', 'b', class_='flex-con xs-pad-lr')
print(element)
# print(res)



