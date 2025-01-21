import requests




# Список имен
names = ["Елена", "Владимир", "3453456", "Саша", "авыавыаыенг"]

# Функция для получения данных о поле по имени
def get_gender_info(name):
    # Отправка запроса к API
    response = requests.get(f'https://api.genderize.io?name={name}')
    data = response.json()
    return data.get('gender', 'не определен'), data.get('probability', 0)



# Запись результатов в файл
with open('names.txt', 'w', encoding='utf-8') as file:
    for name in names:
        gender, probability = get_gender_info(name)
        if probability > 0:
            probability_percentage = f"{probability * 100:.0f}%"
            file.write(f'Имя - {name}\n')
            file.write(f'Пол - {gender}\n')
            file.write(f'Вероятность - {probability_percentage}\n\n')
        else:
            file.write(f'Имя - {name}\n')
            file.write('Пол - не определен\n')
            file.write('Вероятность - не определена\n')
            file.write('Некорректное имя!\n\n')

print("Информация записана в файл names.txt")