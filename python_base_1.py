# 1. Типы данных:

# Integer (int) - целые числа
a = 6
b = 2
c = a + b
d = a / b
e = a % b

print(c)
print(d)
print(e)
print(b**2) # возведение в степень

# Float (float) - вещественные числа (числа с плавающей точкой)
float_a = 0.5
float_b = 1.25

print(type(a))
print(type(float_a))

# Boolean - логический тип данных
is_active = True
is_logout = False

print(id(a)) # id - функция, которая показывает адрес ячейки памяти
print(is_active or is_logout) # or - логическая "или"
print(is_active and is_logout)
print(not is_active and is_logout) # not - логическое отрицание

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# приведение строки к типу int
age = '15'
year = '2024'
print(int(age) + int(year))

# String - (str) - строковый тип данных
text = "I 'love' Python!"
# text = text + " a"
# text += " a" - тоже самое, что text = text + " a"
print(text + ' a')

# None

flag = None

# 2. Структура данных:
# списки - list() - []

cars = ['bmw', 'audi', 24, True, [1,2]]

# словари - dict() - {}
info = {
    'name': 'Alex',
    'cars': cars, # без кавычек пишутся переменные
}

# кортежи  - tuple() - () - неизменяемый список. Как создали так и остается, добавить ничего нельзя!
colors = (
    ('red', '255,0,0'),
    ('blue', '0,0,255')
)

# set - set() - множества - {}

set_numbers = {1, 2, 3, 4, 5, 5, 5, 5, 5, 6}
print(set_numbers) # автоматически удалил дубликаты

# функции
# файлы
# классы
name = 5
Name = 6

'''
Многострочный коментарий
ffdfdjdjdkfj
dfjhfjhdjf
fjdkfjdjfkl
fkdjfkjdfkfj
'''

text_many_lines = """kflkfrk
rkofkrokfokf
jfrkjfkfj
fjkfjkfrjfklrfk"""

number = 6
print(number)

# ввод данных из консоли
name = input("Введите свое имя ")
age = input("Введите свой возраст ")

print(type(age))
