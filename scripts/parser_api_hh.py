import requests


def get_vacancies_data(url: str):
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
    pass






url_api = "https://api.hh.ru/vacancies"
get_vacancies_data(url=url_api)