import requests
import json
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError



# ПОЛУЧЕНИЕ HTML СТРАНИЧКИ!!!
def get_html(url: str) -> str | None:
    try:
        response = requests.get(url)
        status = response.status_code
        # если не успешный запрос и не переадресация то ОШИБКА
        if status != 200 and str(status)[0] != 3: # 404, 503, 301
            print(f"Ошибка запроса. Код ответа - {status}")
            return None
        print(f'Код ответа - {status}')
        html = response.text
        return html
    except ConnectionError as error:
        print('Нет ответа от сервера')
        print('error')
        return None

# ФУНКЦИЯ ПАРСИНГА HTML СТРАНИЧКИ!!!
def parse_html(html: str) -> dict:
    courses = {} # создание пустого словаря

    # доступ к странице
    soup: Bs = Bs(html, 'html.parser')

    # получение даты со страницы и сохранение в переменную
    current_date = soup.find('h2', class_='h2 blue').text.split('\n')[-1].strip()[:10]

    # получение всей таблицы со страницы и сохранение в переменную
    table = soup.find('table', class_='js_sortable')

    # получение всех строк из таблицы и сохранение в переменную
    rows = table.find_all('tr')[2:]

    courses[current_date] = {}
    for row in rows:
        if not row.find('td', class_='t-center'):
            continue
        code = row.find('td', class_='t-center').text
        number_code = code.split()[0]
        txt_code = code.split()[1]

        name = row.find('td', class_='t-left').text.split('\n')[0]
        value = row.find('td', class_='t-right').text.strip() # strip - удалили не нужные символы слева и справа
        print(f'{number_code}-{txt_code} {name} {value}')

        courses[current_date][txt_code] = {
            "number_code": number_code,
            "name": name,
            "value": value
        }
    return courses



def write_data_to_json(data: dict) -> None:
    with open('courses.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_data_from_json(file_patch: str) -> dict:
    with open(file_patch, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


# URL = 'https://www.alta.ru/currency/'
# html = get_html(URL)
# if html:
#     courses = parse_html(html)
#     write_data_to_json(data=courses)

courses_from_file = get_data_from_json('courses.json')
print(courses_from_file)

