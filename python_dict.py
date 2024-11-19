# словарь определяется функцией dict или литералом {}
# словарь хранит данные в формате "ключ: значение"

mydict = dict()

person = {}
person_2 = {'name': 'Elena', 'age': 26}

# получение элемента словаря ИМЯ_СЛОВАРЯ[КЛЮЧ]
print(person_2['name'])


# добавление элемента в словарь ИМЯ_СЛОВАРЯ[КЛЮЧ]=ЗНАЧЕНИЕ
person_2['phone']= '23456'
print(person_2)

person_2['age'] = 43
print(person_2)

print(len(person_2))
person_2['language'] = {'main': 'Russian', 'other': 'English'}
person_2['age'] = ['23456', '678393', '986574']
print(person_2)

person_2[100] = ['23456', '678393', '986574']
print(person_2)

print(list(person_2.keys())[0])
print(list(person_2.values()))

for key in person_2:
    print(key, person_2[key])

#for item in person_2.items():
 #   print(item)
for key in person_2:
    print(f'key - {key}, value - {person_2[key]}')

print(len(person_2))
print(person_2.get('ejhchnj', '404'))
age = person_2.pop('age')
print(age)
print(person_2)

del person_2[100]
print(person_2)

person_1 = person_2.copy()
print(id(person_1))
print(id(person_2))
person_2['new'] = 'new'

print(person_1)
print(person_2)



print(person_2.popitem())
print(person_2.popitem())

a = {}.fromkeys([1, 2, 3], ['a', 'b', 'c'])
print(a)

month_dict = {}
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in month:
    month_dict[i] = f'Month - {i}'

print(month_dict)


users_info = []
N = 3
for i in range(N):
    print(f'Enter {i+1} user s info')
    name = input('Введите имя:')
    age = input('Введите возраст')
    phone = input('Enter the age')
    info = {'name': name,
            'age': age,
            'phone': phone
            }
    users_info.append(info)

    print(users_info)





# x=5
# y=6

# x, y = y,x

# print(x)
# print(y)

# name, age = ('sasha', 25)
# print(name)
# print(age)