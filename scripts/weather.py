import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent



def get_html(url: str) -> str:
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"}
    try:
        response = requests.get(url, headers=headers)
        # если успешный запрос или переадресация то ХОРОШО
        if response.status_code == 200 or str(response.status_code)[0] == '3':
            html= response.text
            # with open("index_1.html", w) as f:
            #     f.write(html)
            return html
        else:
            print(f"Ошибка запроса. Код ответа: {response.status_code}")
            return None
    except ConnectionError as err:
        print(f"Ошибка запроса.\n{err}")
        return None


def get_weather_from_day(html: str) -> dict:
    soup = Bs(html, 'html.parser')
    pass
    weather_info = {}
    day = soup.find('div', class_="dates short-d").text
    weather_info[day] = {}
    table = soup.find('div', class_="weather-short").find("table")
    table_rows = table.find_all('tr')
    for row in table_rows:
        weather_day = row.find('td', class_='weather-day').text





URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
if html:
    get_weather_from_day(html)




# for _ in range(10):
#     print(UserAgent().chrome)

