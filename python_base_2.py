# условное выражение
age = 30
if age < 20:
    print('Error')
    print('Error')
    if age < 15: # if - если. Может быть без ветки else. ":" - то
        print('Fatal')
    else: # else - иначе
        print('not fatal')
elif age < 25: # elif - иначе если, их может быть сколько угодно
    print('<25')
else:
    print('OK')

print('Next')

# цикл for (цыкл счетчиком, безусловный цыкл)

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers: читается для каждого i в коллекции
    print(i)'''

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 10

for i in range(0, N, -1): range - диапазон, -1 - шаг
    print(i)'''


#         0       1       2    индексы
cars = ['bmw', 'audi', 'lada']
#for car in cars:
#    print(car)
for ind in range(len(cars)): # len - функция, которая получает количество элементов
#    print(ind)
#print(cars[0])
#print(cars[-2]) - получение последнего или предпоследнего и т.п. элемента

    print(ind, cars[ind])

a = 10
b = 0
while a < 20: # читается пока a меньше 20
    print(a)
    # a += 1
    b += 1
    # if a == 15:
    if b == 15:
        break





