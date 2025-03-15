"""
Напишите программу, определяющую и выводящую на экран количество
уникальных символов во введенной пользователем строке.
Например, в строке Hello, World! содержится десять уникальных символов,
а в строке zzz – один.
1.Напишите функцию, использующую словарь для решения этой задачи,
2.Напишите функцию, использующую множество для решения этой задачи
"""
def unique_symbols_dict(input_string):
    char_dict = {}
    for char in input_string:
        if char not in char_dict: # проверяю есть ли символ в словаре
            char_dict[char] = 1 # если символ не найден то добавляю его в словарь с начальным значением 1

    unique_count = len(char_dict) # считаю количество уникальных символов и сохраняю их в переменную
    return unique_count
user_input = input("Введите строку: ")
unique_count_dict = unique_symbols_dict(user_input)
print("Количесвто уникальных символов (словарь):", unique_count_dict)


def unique_symbols_set(input_string):
    unique_chars = set(input_string)
    unique_count = len(unique_chars)
    return unique_count

user_input = input("Введите строку: ")
unique_count_set = unique_symbols_set(user_input)
print("Количесвто уникальных символов (словарь):", unique_count_set)
