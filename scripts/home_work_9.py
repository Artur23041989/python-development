import requests
from bs4 import BeautifulSoup as Bs


def parser_website(url):
    response = requests.get(url)
    status = response.status_code
    print(f"Код ответа - {status}")
    html = response.text
    return html

def parser_html(html: str):
    soup = Bs(html, 'html.parser')
    # парсинг товаров
    product_jet_kid = soup.find('a', class_="name_item").text.encode('latin1').decode('utf-8')
    product_band = soup.find_all('a', class_="name_item")[1].text.encode('latin1').decode('utf-8')
    product_black_huawei = soup.find_all('a', class_="name_item")[2].text.encode('latin1').decode('utf-8')
    product_brown_huawei = soup.find_all('a', class_="name_item")[3].text.encode('latin1').decode('utf-8')
    product_runblack_huawei = soup.find_all('a', class_="name_item")[4].text.encode('latin1').decode('utf-8')
    product_grey_huawei = soup.find_all('a', class_="name_item")[5].text.encode('latin1').decode('utf-8')
    product_gold_huawei = soup.find_all('a', class_="name_item")[6].text.encode('latin1').decode('utf-8')
    product_watch = soup.find_all('a', class_="name_item")[7].text.encode('latin1').decode('utf-8')
    # создал список товаров
    product_name = [
        product_jet_kid,
        product_band,
        product_black_huawei,
        product_brown_huawei,
        product_runblack_huawei,
        product_grey_huawei,
        product_gold_huawei,
        product_watch
    ]
    # парсинг цен
    price_jet_kid = soup.find('p', class_='price').text.encode('latin1').decode('utf-8')
    price_band = soup.find_all('p', class_='price')[1].text.encode('latin1').decode('utf-8')
    price_black_huawei = soup.find_all('p', class_='price')[2].text.encode('latin1').decode('utf-8')
    price_brown_huawei = soup.find_all('p', class_='price')[3].text.encode('latin1').decode('utf-8')
    price_runblack_huawei = soup.find_all('p', class_='price')[4].text.encode('latin1').decode('utf-8')
    price_grey_huawei = soup.find_all('p', class_='price')[5].text.encode('latin1').decode('utf-8')
    price_gold_huawei = soup.find_all('p', class_='price')[6].text.encode('latin1').decode('utf-8')
    price_watch = soup.find_all('p', class_='price')[7].text.encode('latin1').decode('utf-8')
    # создание списка цен
    product_price = [
        price_jet_kid,
        price_band,
        price_black_huawei,
        price_brown_huawei,
        price_runblack_huawei,
        price_grey_huawei,
        price_gold_huawei,
        price_watch
    ]
    # объединяю элементы из списков
    product_price_list = [[name, price] for name, price in zip(product_name, product_price)]
    # форматирование строк
    formatted_list = [f"{name} - {price}" for name, price in product_price_list]
    return formatted_list


URL = "https://parsinger.ru/html/index1_page_1.html"
html = parser_website(URL)
parser_html(html)

result = parser_html(html) # заношу функцию в переменную
for item in result:
    print(item)
