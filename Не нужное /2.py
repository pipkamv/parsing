import requests
import fake_useragent
from bs4 import BeautifulSoup
import random

session = requests.Session()
link = 'https://app.inventorysource.com/#/login'
user = fake_useragent.UserAgent().random


header = {
    'user-agent':user
}


data = {
    'login' : 'aruslan@rubekstore.com',
    'password': 'almaty1999',
}

response = session.post(link, data={'login':'aruslan@rubekstore.com','password':'almaty1999'}, headers=header)
print(response.status_code)
print(response.url)





