# 1. Функция, которая принимает два списка и возвращает список, состоящий из общих элементов

def common_elements(list1, list2):
    common = set(list1) & set(list2)
    return list(common)
list_a = [1, 4, 5, 6, 4, 4]
list_b = [2, 7, 9, 1, 4, 5]
result = common_elements(list_a, list_b)
print(result)




# 2. Функция, которая принимает два списка и возвращает список, состоящий из всех элементов 1 и 2 списка,
# кроме общих элементов

def all_elements(list1, list2):
    common = set(list1) | set(list2)
    return list(common)
list_a = [1, 4, 5, 6, 4, 4]
list_b = [2, 7, 9, 1, 4, 5]
result = all_elements(list_a, list_b)
print(result)




# 3. Функция, которая принимает строку и возвращает это строку в нижнем регистре

def registr_string(str):
    return str.lower()
s = "ВОЗВРАЩАЮ СТРОКУ В НИЖНИЙ РЕГИСТР!"
result = registr_string(s)
print(result)




# 4. Функция, которая возвращает список строк и возвращает СТРОКУ,
# состоящую из элементов списка, разделенных подстрокой'---'
# (Например, ['a', 'b', 'c'] -> "a---b---c")

def strings(s):
    return '---'.join(s)
result = strings(['a', 'b', 'c', 'd'])
print(result)





