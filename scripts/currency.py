import requests
from bs4 import BeautifulSoup as Bs


def get_html(url: str) -> str:
    response = requests.get(url)
    status = response.status_code
    print(f'Код ответа - {status}')
    html = response.text
    return html

def parse_html(html: str):
    soup: Bs = Bs(html, 'html.parser')
    current_date = soup.find('h2', class_='h2 blue').text.split('\n')[-1].strip()[:10]
    pass



URL = 'https://www.alta.ru/currency/'
html = get_html(URL)
parse_html(html)

