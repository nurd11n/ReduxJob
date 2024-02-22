import json

import requests
from bs4 import BeautifulSoup

# Загрузите XHTML-страницу с помощью библиотеки requests
url = 'http://zakupki.gov.kg/popp/view/plan/before-sign.xhtml'  # Замените на URL вашей целевой страницы
response = requests.get(url)

# Проверьте успешность запроса
if response.status_code == 200:
    xhtml = response.text
    soup = BeautifulSoup(xhtml, 'lxml')  # lxml - один из парсеров Beautiful Soup

    # Теперь вы можете выполнять поиск и извлекать данные из страницы
    # Например, найдем все заголовки h1 и выведем их текст
    h1_elements = soup.find_all('td')
    for h1 in h1_elements:
        print(h1.text)
        with open('db.json', 'a') as files:
            json.dump(h1, files)
    # print(xhtml)# Получите текст страницы в формате XHTML
else:
    print("Не удалось загрузить страницу")
    xhtml = None

# Если страница была успешно загружена, начните парсинг с использованием Beautiful Soup
# if xhtml:
#     # Создайте объект Beautiful Soup для разбора
#     soup = BeautifulSoup(xhtml, 'lxml')  # lxml - один из парсеров Beautiful Soup
#
#     # Теперь вы можете выполнять поиск и извлекать данные из страницы
#     # Например, найдем все заголовки h1 и выведем их текст
#     h1_elements = soup.find_all('h1')
#     for h1 in h1_elements:
#         print(h1.text)

    # Можно выполнять другие операции парсинга по аналогии с примерами, которые я рассматривал ранее.
