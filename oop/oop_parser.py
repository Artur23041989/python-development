import json
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent


# ПРИМЕР КОДА ДЛЯ ПАРСИНГА
class Parser:
    def __init__(self, url):
        self.url = url
        self.data_weather = {}
        # self.data_vacancies = []
        self.html = None

    def get_html(self):
        headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"}
        try:
            response = requests.get(self.url, headers=headers)
            # если успешный запрос или переадресация то ХОРОШО
            if response.status_code == 200 or str(response.status_code)[0] == '3':
                self.html = response.text
                return self.html
            else:
                print(f"Ошибка запроса. Код ответа: {response.status_code}")
                return None
        except ConnectionError as err:
            print(f"Ошибка запроса.\n{err}")
            return None

    def parse_html(self):
        self.get_html()
        soup = Bs(self.html, "parser.html")
        day = soup.find('div', class_="dates short-d").text
        table = soup.find('div', class_="weather-short").find("table")
        table_rows = table.find_all('tr')
        for row in table_rows:
            weather_day = row.find('td', class_='weather-day').text

            self.data_weather[day][weather_day] = {}

            weather_temperature = row.find('td', class_='weather-temperature').text
            weather_type = row.find('div', class_='wi')['title']
            weather_feeling = row.find('td', class_='weather-feeling').text
            weather_probability = row.find('td', class_='weather-probability').text
            weather_pressure = row.find('td', class_='weather-pressure').text
            weather_wind = row.find('td', class_='weather-wind').text
            weather_nw = row.find('span', class_='tooltip')['title']
            weather_humidity = row.find('td', class_='weather-humidity').text

            self.data_weather[day][weather_day]['weather_temperature'] = weather_temperature
            self.data_weather[day][weather_day]['weather_type'] = weather_type
            self.data_weather[day][weather_day]['weather_feeling'] = weather_feeling
            self.data_weather[day][weather_day]['weather_probability'] = weather_probability
            self.data_weather[day][weather_day]['weather_pressure'] = weather_pressure
            self.data_weather[day][weather_day]['weather_wind'] = weather_wind
            self.data_weather[day][weather_day]['weather_nw'] = weather_nw
            self.data_weather[day][weather_day]['weather_humidity'] = weather_humidity
        return self.data_weather





    # def write_data_to_file(self):
    #     with open("file.txt", "w") as f:
    #         json.dump(self.data_weather, f, indent=2)

parser_weather = Parser(url="https://world-weather.ru/pogoda/russia/saint_petersburg/7days/")
# parser_weather.parse_html()


