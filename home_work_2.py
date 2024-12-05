# 1. Даны списки [1,2,3,4,5] и [3,4,5,6,7,8]

# Выводим на экран общие элементы списков
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7, 8]
# первый способ
# c = []
# for i in a: # извлекаем элемент из списка "а"
#     if i in b: # если есть одинаковые элементы в списке "b"
#         c.append(i) # то добавляем их в список "с"
# второй способ
c = list(set(a)&set(b))
print(*c)

# Выводим элементы, которые есть в первом списке, но нет во втором
c = list(set(a).difference(set(b)))
print(*c)



# 2. Пользователь вводит с клавиатуры марку машины, модель, год выпуска, цвет
# Сохраните введенные данные в словарь с соответствующими ключами.
# Выведите:
# - список ключей словаря
# - список значений словаря
# - элементы в формате ключ -> значение
#   (f-строка)
brand = input('Введите марку машины: ')
model = input('Введите модель машины: ')
year = input ('Введите год выпуска машины: ')
color = input('Введите цвет машины: ')
car_info = {
    'Марка': brand,
    'Модель': model,
    'Год выпуска': year,
    'Цвет': color
}
print('Список ключей словаря: ', list(car_info.keys()))
print('Список значений словаря: ', list(car_info.values()))
print('Элементы в формате ключ: значние: ')
for key, value in car_info.items():
    print(f'{key}: {value}')
