import json

import requests
from bs4 import BeautifulSoup

url = 'http://cbd.minjust.gov.kg/act/view/ru-ru/112361'
response = requests.get(url)

if response.status_code == 200:
    xhtml = response.text
    soup = BeautifulSoup(xhtml, 'lxml')
    h1_elements = soup.find_all('span')
    for h1 in h1_elements:
        print(h1.text)
else:
    print("Не удалось загрузить страницу")
    xhtml = None


if xhtml:
    soup = BeautifulSoup(xhtml, 'lxml')
    h1_elements = soup.find_all('h1')
    for h1 in h1_elements:
        print(h1.text)
