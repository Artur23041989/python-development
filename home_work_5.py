# 1. Напишите функцию, которая принимает три параметра - цифры и
# выводит на экран их сумму, произведение, наибольшее и
# наименьшее число

def accepts_number(num1, num2, num3):
    summ = num1 + num2 + num3 # суммируем
    product = num1 * num2 * num3 # умножаем
    max_num = max(num1, num2, num3) # находим наибольшее число
    min_num = min(num1, num2, num3) # находим наименьшее число
    print(f'Сумма: {summ}')
    print(f'Произведение: {product}')
    print(f'Наибольшее число: {max_num}')
    print(f'Наименьшее число: {min_num}')
accepts_number(8, 4, 11)



# 2. Напишите функцию, которая принимает на вход строку, введенную
# пользователем.
# Функция должна:
# 1. Посчитать, сколько слов в строке (разделенных пробелом)
# 2. Посчитать, сколько слов, в которых более 2 символов
# 3. Вывести все эти значения с пояснениями, а также вывести
# введенную строку в нижнем регистре и в верхнем регистре

def string(user_input):
    words = user_input.split() # разделяем слова по пробелам
    total_words = len(words) # считаем количесвто слов в строке
    long_words = sum(1 for word in words if len(word) > 2) # считаем количество слов где больше 2 символов
    print(f'Количество слов в строке: {total_words}')
    print(f'Количесвто слов в строке, в которых более 2 символов: {long_words}')
    print(f'Вывод строки в нижнем регистре: {user_input.lower()}')
    print(f'Вывод строки в верхнем регистре: {user_input.upper()}')
user_input = input('Введите текст: ')
string(user_input)



# 3. Дан список [1,30,30,25,24,30,1,27,25,40]. Выведите на экран только
# уникальные числа этого списка. Создайте новый список и добавьте в
# него только числа большие 24. Выведите его на экран. Создайте
# словарь, в котором ключами являются порядковые номера
# элементов, а значениями этих ключей четные цифры со второго
# списка.
# Например, {‘1’: 24, ‘2’: 28, ‘3’: 30}

numbers = [1,30,30,25,24,30,1,27,25,40]
uniqal_numbers = set(numbers) # set - находим уникальные числа
print('Вывод уникальных чисел:', uniqal_numbers)
# создание списка с числами больше 24
filter_numbers = [num for num in uniqal_numbers if num > 24]
print('Числа больше 24:', filter_numbers)

numbers_dict = {} # создаем пустой словарь
numbers_index = 1 # начало ключей с 1
for num in filter_numbers:
    if num % 2 == 0:
        numbers_dict[numbers_index] = num
        numbers_index += 1
print('Словарь с четными числами:', numbers_dict)



# 4. Напишите функцию, которая принимает число - сантиметры и
# возвращает количество метров (десятичное)

def num_centimetr(centimetr):
    metr = centimetr / 100 # переводим сантиметры в метры
    return metr
cm_value = 420
metr_value = num_centimetr(cm_value)
print(metr_value)




# 5. Напишите функцию для пересчёта величины временного интервала,
# заданного в минутах, в величину, выраженную в часах и минутах.
# Пример: my_func(90) -> 1 час 30 минут

def convert_min_to_hour_min(minutes):
    hours = minutes // 60 # получаем количество часов
    remaining_minutes = minutes % 60 # получаем оставшиеся минуты
    return f'{hours} час(ов) {remaining_minutes} минут(ы)' # возвращаем время в часах и минутах
input_minutes = 110
result = convert_min_to_hour_min(input_minutes)
print(result)




# 6. Напишите функцию, в которой рассчитывается сумма и
# произведение цифр положительного трёхзначного числа.
# Пример: my_func(132) -> Сумма цифр = 6, Произведение цифр = 6

def calculate_sum_and_product(number):
    digits = [int(digit) for digit in str(number)] # из числа делаем строку и извлекаем цыфры
    sum_digits = sum(digits) # склаываем числа
    # умножаем числа
    product_digits = 1
    for digit in digits:
        product_digits *= digit

    return f'Сумма цыфр = {sum_digits}. Произведение цыфр = {product_digits}'
result = calculate_sum_and_product(132)
print(result)



# 7. Напишите функцию, которая принимает три целых числа: x, a, b и
# определяет, принадлежит ли число x промежутку от a до b.

def numb(x, a, b):
    return min(a, b) <= x <= max(a, b)
x = 20
a = 4
b = 11
if numb(x, a, b):
    print(f'Число {x} принадлежит промежутку от {a} до {b}')
else:
    print(f'Число {x} не принадлежит промежутку от {a} до {b}')



# 8. Функция принимает две строки: txt_1 и txt_2. Если количество
# символов в этих строках одинаковое, то сделайте из этих строк
# словарь так, чтобы символы первой строки стали ключами, а
# символы второй строки - значениями.
# Например: txt1 = 'abcde' txt2 = '12345'
# Результат функции:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def accepts_strings(txt1, txt2):
    # if len(txt1) != len(txt2):
    #     return 'Ошибка! Длина строк разная.'

    # создаем словарь и одновременно меняем значения в целые числа
    result_dict = {txt1[i]:int(txt2[i]) for i in range(len(txt1))}
    return result_dict
txt1 = 'abcde'
txt2 = '12345'
result = accepts_strings(txt1, txt2)
print(result)



# 9. Напишите программу, которая принимает от пользователя ФИО,
# возраст и номер телефона, которые он ввел с клавиатуры.
# Эти значения - входные параметры для функции.
# Функция должна выполнять следующие действия:
# - проверять, что возраст от 1 года до 150 лет (в случае большего или
# меньшего возраста выдавать предупреждение и сохранять возраст,
# равный 0)
# - проверять, что номер телефона от 4 до 11 символов (в случае
# неправильного количества цифр в номере сохранять номер
# 8-000-000-00-00
# - все значения функция должна сохранить в словарь с
# соответствующими ключами и вернуть его

def data_user_info(fio, age, phone):
    # проверяю возраст от 1 до 150
    if 1 <= age <= 150:
        valid_age = age
    else:
        print('Возраст не от 1 до 150!!! Сохранение возраста - 0.')
        valid_age = 0
    # проверяю номер телефона от 4 до 11 символов
    if 4 <= len(phone) <= 11:
        valid_phone = phone
    else:
        print('Неправильное количество цифр в номере! Сохраняется - 8-000-000-00-00')
        valid_phone = '8-000-000-00-00'
    # создание словаря с результатами
    user_info = {
        'ФИО': fio,
        'Возраст': valid_age,
        'Телефон': valid_phone
    }
    return user_info
# Ввод данных пользователем
fio = input('Введите Ваше ФИО: ')
age = int(input('Введите Ваш возраст: '))
phone = input('Введите Ваш номер телефона: ')
result = data_user_info(fio, age, phone)
print(result)



# 10. Дана строка “Python is the best programming language”.
# Выведите на экран следующие данные:
# 1. Количество символов в строке
# 2. Первый элемент строки
# 3. Последний элемент строки
# 4. Первое слово этой строки
# 5. Последнее слово этой строки
# 6. Слово programming, используя срез строки

my_line = 'Python is the best programming language'
print('Количество символов в строке:', len(my_line))
print('Первый элемент строки', my_line[0])
print('Последний элемент строки', my_line[-1])
print('Первое слово этой строки', my_line.split()[0])
print('Последнее слово этой строки', my_line.split()[-1])
print('Слово programming, используя срез строки:', my_line[19:31])


# 11. Калькулятор: Напишите функцию calculator(operation, a, b), которая
# принимает строку с операцией ('add', 'subtract', 'multiply', 'divide') и два
# числа. Функция должна выполнять соответствующую операцию и
# возвращать результат.

def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiplay':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Ошибка! Деление на ноль.'
        return a / b
print(calculator('add', 5, 8))
print(calculator('subtract', 5, 8))
print(calculator('multiplay', 5, 8))
print(calculator('divide', 5, 0))
print(calculator('divide', 5, 8))