import requests
from bs4 import BeautifulSoup
import csv


url_login = 'https://app.inventorysource.com/#/login'
url_main = 'https://app.inventorysource.com/'

client = requests.session()
html = client.get(url_login)
cookies = html.cookies.get_dict()
soup = BeautifulSoup(html.text, 'lxml')

login_csrf = soup.find('input', dict(name='c48e30a0-69ce-4e37-b522-c7f5546f07d0'[0]))

payload = {
    'form_sent': '1',
    'login': "aruslan@rubekstore.com",
    'password': "almaty1999",
    '_csrf': login_csrf
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Referer': url_main,
    'Connection': 'keep-alive',
}

r = requests.post(url_login, data={'login':'aruslan@rubekstore.com','password':'almaty1999'}, headers=headers)

print(r.status_code)
print(r.url)

