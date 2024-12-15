import os
'''
1. Пользователь вводит с клавиатуры имя, фамилию, телефон (повторить 3 раза)
записать полученную информацию в  каталог user_info, в файл users.txt, отделяя информацию о каждом пользователе строкой '---------------------'
Формат записи:
Пользователь 1:
Имя - Антон
Фамилия - Иванов
Телефон - 454356546
__________________
Пользователь 2:
Имя - Антон
Фамилия - Иванов
Телефон - 454356546
'''

# создаю каталог с названием "user_info"
dir_name = 'user_info'
if not os.path.exists(dir_name): # функция проверки наличия папки с именем user_info
    os.makedirs(dir_name) # если данная папка не существует то она создаcтся

with open(os.path.join(dir_name, 'users.txt'), 'w', encoding='utf-8') as file:
    for i in range(1, 4): # цикл для повтора ввода данных пользователем 3 раза
        name = input(f'Введите имя {i}: ')
        surname = input(f'Введите фаимлию {i}: ')
        phone = input(f'Введите телефон {i}: ')

        # записываю содержимое в файл user.txt с использованием метода file.write
        file.write(f'Пользователь {i}:\n')
        file.write(f'Имя - {name}\n')
        file.write(f'Фамилия - {surname}\n')
        file.write(f'Телефон - {phone}\n')
        file.write(f'__________________\n')


'''
2. Создать файл numbers.txt в каталоге numbers
Записать в него числа следующим образом:
в каждой строке два числа, разделенные пробелом

1 число увеличивается от 1 до 10 с каждой новой строкой
2 число уменьшается от 10 до 1 с каждой новой строкой

Формат записи:
1 10
2 9
3 8
4 7
...
10 1
'''
os.makedirs('numbers', exist_ok=True) # создаю папку numbers
myfile = open('numbers/numbers.txt', mode='w', encoding='utf-8') # создаю в папке numbers файл numbers.txt
for i in range(1, 11): # цикл от 1 до 10 включительно
    myfile.write(f'{i} {11 - i}\n') # запись в файл в формате из задачи
myfile.close()



'''
3. Считать файл numbers.txt
3.1. Написать функцию, которая возвращает сумму произведенй чисел в каждой строке:
     1*10 + 2*9 + 3*8 + ... + 10*1
3.2. Написать функцию, которая выводит числа из правого столбца (в том же порядке)
3.4 Результат работы каждой функции записать в файл numbers_result.txt в каталоге numbers
'''

def sum_of_products(lines):
    total_sum = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        # line.split() разбивает строку на отдельные подстроки (числа в виде строк) по пробелам.
        # map(int, ...) преобразует каждую подстроку в целое число.
        # list(...) создаёт список из этих целых чисел.
        total_sum += sum(x * y for x, y in zip(numbers, reversed(numbers)))
    return total_sum

def extract_right_column(lines):
    return [line.split()[-1] for line in lines]

def main():
    # Считываем файл
    with open('numbers/numbers.txt', 'r') as file:
        lines = file.readlines()

    # Убираем лишние пробелы и переносы
    lines = [line.strip() for line in lines if line.strip()]

    # Вычисляем результаты
    sum_prod = sum_of_products(lines)
    right_column = extract_right_column(lines)

    # Записываем результаты в файл
    with open('numbers/numbers_result.txt', 'w') as result_file:
        result_file.write(f"Сумма произведений: {sum_prod}\n")
        result_file.write("Числа из правого столбца: " + ' '.join(right_column) + "\n")

