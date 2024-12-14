from functools import reduce

def subtract(x):
    return x - 2
numbers = [6, 8, 4, 1, 7]
sub_numbers = list(map(subtract, numbers)) # map применяется к каждому элементу списка
print("Вычитание чисел:", sub_numbers)



def check_even_numbers(x):
    return x % 2 == 0 # возвращаем четные числа
numbers = [11, 12, 13, 17, 20, 36] # список чисел
even_numbers = list(filter(check_even_numbers, numbers))
print("Четные числа:", even_numbers)



def sum(x, y):
    return x + y
numbers = [17, 21, 3, 24, 5]
# Применяем функцию sum к элементам списка
product = reduce(sum, numbers)
print("Сумма чисел:", product)
