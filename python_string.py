s1 = 'Hello world1'
s2 = "Hello world2"
s3 = """Hello world3"""
print(type(s1))
print(type(s2))
print(type(s3))




s1 = 'Py'
s2 = 'thon'
s3 = s1 + s2
print(s3)




s1 = 'Googlechrom'
s2 = 'chrom'
s3 = s1.replace('chrom', 'xxx') # создание новой строки путём замены частей исходной строки
print(s3)




# дублирование строки
s = 'world ' * 5
print(s)




# проверка есть ли в составе строки нужный фрагмент
s1 = 'Иванушкин Артур Игоревич, 1989 года рождения'
s2 = '1989 года рождения'
if s2 in s1: # есть ли содержимое строки s2 в строке s1
    print('Ok, в строе имеется год рождения')
else:
    print('Error')




st = 'a'
if st in 'abcd':
    print('YES')




# определние длины строки
ln = 'Python'
print(len(ln))

s5 = len('Hit')
print(s5)




# поиск символов по индексу
st = 'Ivan'
print(st[0])
print(st[1])
print(st[2])
print(st[3])

print(st[-1])
print(st[-4])




# получаем часть строки (срез строки) st[начальный индекс:конечный индекс]
st = 'Windows'
print(st[0:3])
print(st[3:5])
print(st[5:6])
print(st[:6]) # с начала строки до индекса 6 не включая его
print(st[4:]) # до конца строки с индекса 4 включая его
print(st[:]) # вся строка
print(st[2:2]) # выводит пустые строки
print(st[5:3]) # выводит пустые строки

# срез с отрицательными индексами
print(st[-5:-1])
print(st[-3:-3]) # выводит пустые строки
print(st[0:7:2]) # срез строки с шагом 2



# вывод символов строки в обратном порядке
st = 'ноутбук'
print(st[::-1])



# Методы поиска подстроки
s = 'Windowswindows'
st = 'ind'
print(s.find(st)) # возвращает индекс первого совпавшего значения подстроки
print(s.rfind(st)) # возвращает индекс последнего совпавшего значения подстроки



# Методы преобразования строки в верхний и нижний регистры
s = 'Mutter'
print(s.upper())
print(s.lower())
print(s)


# Метод разбиения строки по разделителю
st = 'scihub cats,dogs hamster man'
print(st.split(','))
print(st.split(' '))



# Методы rjust() и ljust() увеличиваею строку и заполняют символами
s = 'Hello!'
print(s.rjust(8,'*'))
print(s.ljust(8,'*'))






