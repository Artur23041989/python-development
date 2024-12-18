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
    # собираю ссылки на нумерацию страниц на сайте
    # способ 1
    link_page_1 = soup.find('a', href="index1_page_1.html").text
    link_page_2 = soup.find('a', href="index1_page_2.html").text
    link_page_3 = soup.find('a', href="index1_page_3.html").text
    link_page_4 = soup.find('a', href="index1_page_4.html").text
    print(link_page_1, link_page_2, link_page_3, link_page_4)

    # способ 2
    links_page = soup.find_all('div', class_="pagen")[1].text.split()
    print(*links_page)

    # собираю ссылки на категории товаров


    pass





URL = "https://parsinger.ru/html/index1_page_1.html"
html = parser_website(URL)
parser_html(html)


