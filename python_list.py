# Создание списка
# С использование функции list()
user = list()

# С использованием литерала []
# index      0     1 (-2)   2 (-1)
# Доступ к элементам списка
users_2 = ['Dima', 'Vova', 'Elena']
print(users_2[0])
print(users_2[-1])
print(users_2[1])
#print(users_2[4]) # выдаст ошибку

# добавление элементов в список
users_2.append('Olga')

# расширение списк аэлементами другого списка
users_2 += ['Sasha', 'Masha']
users_2.extend(['Natasha','Sveta'])


# добавление элемента в произвольное место
users_2.insert(0, 'Zero')
users_2.insert(-1, 'Last')
#users_2.insert(len(users_2), 'Last!!!")
print(users_2)

# получение количества элементов списка
print(len(users_2))

# pop - удалить элемент и получить его
print(users_2.pop(0))

# count - подсчет количества элементов в списке
print(users_2.count('Sasha'))

# users_2.remove('Sasha') (первого, которого нашел)
print(users_2)

# получение индекса элемента по его значению (первого, которого нашел)
print(users_2.index('Sasha', 2, 5))

# users_2.clear() удаление элементов списка

users_3 = [1,2,3,4]
print(users_2 + users_3)

# in - оператор для проверки наличия элемента в список
name = 'Sasha'
if name  in users_2:
    print('ok')
else:
    print('not found')

print(id(users_2))
users_2.append('XXX')
print(id(users_2))

