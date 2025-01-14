import json
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent



def get_html(url: str) -> str | None:
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"}
    try:
        response = requests.get(url, headers=headers)
        # если успешный запрос или переадресация то ХОРОШО
        if response.status_code == 200 or str(response.status_code)[0] == '3':
            html= response.text
            return html
        else:
            print(f"Ошибка запроса. Код ответа: {response.status_code}")
            return None
    except ConnectionError as err:
        print(f"Ошибка запроса.\n{err}")
        return None

def get_weather_from_day(html: str) -> dict:
    soup = Bs(html, 'html.parser')
    weather_info = {}
    day = soup.find('div', class_="dates short-d").text
    weather_info[day] = {}
    table = soup.find('div', class_="weather-short").find("table")
    table_rows = table.find_all('tr')
    for row in table_rows:
        weather_day = row.find('td', class_='weather-day').text

        weather_info[day][weather_day] = {}

        weather_temperature = row.find('td', class_='weather-temperature').text
        weather_type = row.find('div', class_='wi')['title']
        weather_feeling = row.find('td', class_='weather-feeling').text
        weather_probability = row.find('td', class_='weather-probability').text
        weather_pressure = row.find('td', class_='weather-pressure').text
        weather_wind = row.find('td', class_='weather-wind').text
        weather_nw = row.find('span', class_='tooltip')['title']
        weather_humidity = row.find('td', class_='weather-humidity').text

        weather_info[day][weather_day]['weather_temperature'] = weather_temperature
        weather_info[day][weather_day]['weather_type'] = weather_type
        weather_info[day][weather_day]['weather_feeling'] = weather_feeling
        weather_info[day][weather_day]['weather_probability'] = weather_probability
        weather_info[day][weather_day]['weather_pressure'] = weather_pressure
        weather_info[day][weather_day]['weather_wind'] = weather_wind
        weather_info[day][weather_day]['weather_nw'] = weather_nw
        weather_info[day][weather_day]['weather_humidity'] = weather_humidity
    return weather_info

def write_data_to_json(data: dict) -> None:
    with open('weather.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
if html:
    data = get_weather_from_day(html)
    write_data_to_json(data)



'''
weather_info = {
    'Понедельник, 13 января': {
        "Ночь": {
        }
    }
}
'''


# for _ in range(10):
#     print(UserAgent().chrome)

