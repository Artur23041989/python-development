import requests



# получаем с помощью функции картинку
def get_image_link(url: str) -> str:
    resp = requests.get(url)
    data = resp.json()
    link = data.get("message")
    return link

# функция для скачивания картинки
def download_image(url: str) -> None:
    print(url)
    resp = requests.get(url)
    image = resp.content
    with open("image.jpg", "wb") as f:
        f.write(image)



# https://dog.ceo/api/breeds/image/random
# /api/breeds/image/random - PATH-param (параметры пути)


# https://api.genderize.io?name=misha
# ? - отделяет домен от QUERY - параметров
# name=misha = QUERY-param (параметр запроса)
# mvideo.ru/products?brand=samsung&model=galaxy&price_from=1000&price_to=40000



api_url = "https://dog.ceo/api/breeds/image/random"
link = get_image_link(url=api_url)
download_image(url=link)

