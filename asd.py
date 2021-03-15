import lxml
import requests
from bs4 import BeautifulSoup
import json
import csv

debug = 'https://app.inventorysource.com/views/supplier/index.html'
session = requests.Session()
auth = session.post('https://app.inventorysource.com/#/login', data={'login':'aruslan@rubekstore.com','password':'almaty1999'})
res = session.get(debug)
soup = BeautifulSoup(res)
element = soup.find('div', 'b', class_='flex-con xs-pad-lr').contents
print(element)


def get_html(url):
    r = requests.get(url)
    return r.text

def refinder(s):
    r = s.split('')
    result = r.replace(':', '')
    return result

def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(str(data['name']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    pop = soup.find('div', class_='flex-con xs-pad-lr')

    for po in pop:
        name = po.find('b')
        data = {'name':name}
        write_csv(data)

def main():
    url = 'https://app.inventorysource.com/views/supplier/index.html'
    get_data(get_html(url))


if __name__ == '__main__':
    main()