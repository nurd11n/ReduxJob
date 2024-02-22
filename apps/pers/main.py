import requests
from bs4 import BeautifulSoup as bs
import json
import csv
import re


def get_html(url):
    response = requests.get(url)
    return response.text


def write_to_json(data):
    # with open('data1.json', 'a', encoding='utf8') as files:
    #     json.dump(data, files)
    # with open('test.txt', 'a') as file:
    #     file.write(data)
    with open('data1.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['id'], data['Номер счета'], data['Наименование счета'], data['Сумма'], data['год']])

def get_data(html):
    soup = bs(html, 'lxml')
    names = soup.find('div', class_='ui-datatable-tablewrapper').find_all('td')
    # print(names)
    for name in names:
        try:
            text = name.find_next('td').text
            # print(text)
            id = []
            chet = []
            naming = []
            cash = []
            yars = []
            for i in text.split():
                if i == 'ID':
                    id.append(i)
                if i == 'Номер счета':
                    chet.append(i)
                if i == 'Наименование счета':
                    naming.append(i)
                if i == 'Сумма':
                    cash.append(i)
                if i == 'год':
                    yars.append(i)

            data = {
                "id": id,
                "Номер счета": chet,
                "Наименование счета": naming,
                "Сумма": cash,
                "год": yars
            }
            write_to_json(data)

            pattern_id = r"ID(\d+)"
            pattern_reserved_sum = r"Номер счета(\d+)"
            pattern_saved_sum = r"Наименование счета(\d+)"
            pattern_sum = r"Сумма(\d+)"
            pattern_year = r"год(\d+)"

            # Функция для извлечения значений из текста с использованием регулярных выражений
            def extract_value(text, pattern):
                match = re.search(pattern, text)
                if match:
                    return match.group(1)  # Возвращает значение, найденное в скобках

            # Извлеките значения
            sum_value = extract_value(text, pattern_sum)
            reserved_sum_value = extract_value(text, pattern_reserved_sum)
            saved_sum_value = extract_value(text, pattern_saved_sum)
            balance_value = extract_value(text, pattern_id)
            year_value = extract_value(text, pattern_year)

            # Выведите результат
            print(f"Id: {balance_value}")
            print(f"Сумма: {sum_value}")
            print(f"Номер счета: {reserved_sum_value}")
            print(f"Наименование счета: {saved_sum_value}")
            print(f"Год: {year_value}")
        except: print("error")



        # data = {
        #     'datas': title
        #     # 'price': price,
        #     # 'image': image,
        #     # 'mileage': mileage,
        #     # 'desc': desc
        # }
        # write_to_json(data)


def main():
    url = 'http://zakupki.gov.kg/popp/view/plan/before-sign.xhtml'
    html = get_html(url)
    get_data(html)

main()

# for row in n ('tr'):  # Выбираем каждую строку
#     print(row)
#     span_element = row.css('td span::text').get()  # Извлекаем текст из <span>
#     if span_element:
#         value = row.css('td::text').get()  # Извлекаем текст из <td> после <span>
#         yield {'element': span_element, 'value': value}

# for name in names:
# try:
#     title = name.find('td').text
# except AttributeError:
#     title = ' '
# print(title),
# try:
#     price = car.find('span', class_="catalog-item-price").text.strip()
# except AttributeError:
#     price = ' '
#
#    print(price)
