import requests
from random import randint
import os
from time import sleep
import random



api_url = "https://dog.ceo/api/breeds/image/random"

# Путь к директории, где будут сохраняться изображения
save_dir = "dog_images"

# Количество изображений для загрузки
image_count = 30

# Создаем директорию, если ее нет
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def download_dog_images(count):
    breeds_collected = set()  # Множество для хранения уникальных пород
    images_downloaded = 0

    while images_downloaded < count:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            breed = data['message'].split('/')[-2]  # Получаем породу из URL картинки
            img_url = data['message']

            # Создаем директорию для породы, если ее еще нет
            breed_dir = os.path.join(save_dir, breed)
            if not os.path.exists(breed_dir):
                os.makedirs(breed_dir)

            # Формируем имя файла
            img_name = f"{breed}_img_{random.randint(1, 1000)}.jpg"
            img_path = os.path.join(breed_dir, img_name)

            # Скачиваем изображение и сохраняем
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as handler:
                handler.write(img_data)

            print(f"{img_path}")

            images_downloaded += 1
            breeds_collected.add(breed)


download_dog_images(image_count)