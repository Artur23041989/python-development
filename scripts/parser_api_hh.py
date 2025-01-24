import requests

# функция возвращает количество результатов, страниц
def get_vacancies_pages(url: str):
    area = 2
    per_page = 100
    text = 'python'

    params = {
        'area': area,
        'per_page': per_page,
        'text': text
    }

    resp = requests.get(url, params=params)
    data = resp.json()
    return data['pages'], data['found'] # количество найденных страниц и результатов

def get_data_page(url: str, page: int): # получает информацию со странички
    params = {
        'area': 2,
        'per_page': 100,
        'page': page,
        'text': 'python'
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data



def parse_page(data: dict): # функция парсит непостредственно старничку
    vacancies = {}
    items = data['items']
    for i in items:
        vacancies[i['id']] = i['name']
    return vacancies

def main(): # главная ф-ция, в которой вызываются предыдущие ф-ции
    vacancies = []
    url_api = "https://api.hh.ru/vacancies"
    pages, found = get_vacancies_pages(url=url_api)
    print(f'Найдено {found} вакансий')
    for i in range(1, 3):
        data_page = get_data_page(url=url_api, page=i)
        vacancies.append(parse_page(data_page))
    print(vacancies, sep='/n')


if __name__ == '__main__':
    main()