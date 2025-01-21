import requests


def get_gender_name(name: str) -> dict:
    url = f"https://api.genderize.io/?name={name}"
    response = requests.get(url)
    data = response.json()
    print(data)

get_gender_name(name="Alena")




def get_gender_data(name: str) -> dict:
    params = {
        "name": name
    }
    url = "https://api.genderize.io/"
    response = requests.get(url, params=params)
    data = response.json()
    return data


def parse_gender_data(data: dict) -> None:
        pass

gender_data = get_gender_data(name='Елена')
print(gender_data)
print(parse_gender_data(data=gender_data))

