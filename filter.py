"""
Django предоставляет богатые возможности по фильтрации данных. Для фильтрации данных у объекта QuerySet могут применяться следующие методы:


get(): получает один объект модели

filter(): получает набор объектов модели, которые соответствуют условию. Результат метода - объект QuerySet

exclude(): получает набор объектов модели, которые НЕ соответствуют условию. Результат метода - объект QuerySet

Все три метода в качестве параметра получают условию, по которому идет фильтрация. Рассмотрим, какие условия мы можем определить.

Допустим, в файле models.py определена следующая модель Person:

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

Самый простый простой тип условия преставляет равенство свойства модели некоторому значению:

from .models import Person

# получаем пользователя по имени
tom = Person.objects.get(name="Tom")
print(f"{tom.name} - {tom.age}")

# получаем пользователей, у которых возраст равен 32
people_by_age1 = Person.objects.filter(age=32)
for person in people_by_age1:
    print(f"{person.name} - {person.age}")

# получаем пользователей, у которых возраст НЕ равен 32
people_by_age2 = Person.objects.exclude(age=32)
for person in people_by_age2:
    print(f"{person.name} - {person.age}")

В первом случае ищем один объект по имени: tom = Person.objects.get(name="Tom")

или поиск по возрасту people_by_age1 = Person.objects.filter(age=32)

Но кроме обычного равенства свойств модели некоторому значению можно применять и другие условия. Они определяются
с помощью спецификатора фильтрации, который указывается в условии после свойства модели через два знака подчеркивания:
свойство__спецификатор = значение

Рассмотрим спецификаторы, которые можно использовать.

exact и iexact
exact выбирает все объекты моделей, в которых свойство равно определенному значению. inexact выполняет ту же самую
задачу, только выборка значений не зависит от регистра:

# получаем пользователя по имени Tom
tom = Person.objects.get(name__exact="Tom")

# получаем пользователей, у которых возраст равен 32
people_by_age = Person.objects.filter(age__exact=32)

# получаем пользователя по имени Tom или tom или TOM
tom = Person.objects.get(name__iexact="Tom")

Стоит учитывать, что в некоторых СУБД, например, в MySQL, поиск по строкам регистрозависимый, то есть "Tom" и "tom" - это две разные строки.
Если необходимо найти данные, где поле таблицы имеет значение NULL, то свойству модели передается значение None:

# получаем пользователей, у которых имя равно NULL
people_by_name = Person.objects.filter(name__exact=None)


contains и icontains
contains находит строки, которые содержат некоторую подстроку, причем поиск регистрозависимый. icontains выполняет
аналогичную задачу, за тем исключением, что поиск не зависит от регистра:

# получаем пользователей, у которых имя содержит букву o
people1 = Person.objects.filter(name__contains="o")

# получаем пользователей, у которых имя содержит букву T или t
people2 = Person.objects.filter(name__icontains="T")

in
in находит модели со свойством, значение которого равно одному из значений из списка:

# получаем пользователей, у которых возраст равен или 32, или 35, или 38,
people = Person.objects.filter(age__in=[32, 35, 38])

gt, gte, lte, lt
Ряд спецификаторов позволяют найти объекты, свойства которых больше или меньше определенного значения:
gt (больше чем), gte (больше чем или равно), lt (меньше чем), lte (меньше чем или равно):

# получаем пользователей, у которых возраст меньше или равен 32
people = Person.objects.filter(age__lte=32)

# получаем пользователей, у которых возраст больше 40
people = Person.objects.filter(age__gt=40)

startswith и istartswith
startswith выбирает объекты моделей со значениями, которые начинаются на определенную строку. Выборка зависит от регистра.

istartswith выполняет ту же задачу, только выборка не зависит от регистра.

# получаем пользователей, у которых имя начинается с To
people = Person.objects.filter(name__startswith="To")

# получаем пользователей, у которых имя начинается с To или to
people = Person.objects.filter(name__istartswith="To")

endswith и iendswith
endswith выбирает объекты моделей со значениями, которые заканчиваются на определенную строку. Выборка зависит от регистра.

iendswith выполняет ту же задачу, только выборка не зависит от регистра.

# получаем пользователей, у которых имя заканчивается на m
people = Person.objects.filter(name__endswith="m")

# получаем пользователей, у которых имя заканчивается на m или M
people = Person.objects.filter(name__iendswith="m")

range
range определяет диапазон, в которое должно входить значение свойства модели:
# получаем пользователей, у которых возраст в диапазоне от 28 до 38 включительно
people = Person.objects.filter(age__range=(28, 38))

isnull
isnull выбирает объекты моделей, у которых поле в таблице имеет значение NULL (при значении True) или, наоборот,
не имеет значение NULL (при значении False)
# получаем пользователей, у которых имя не установлено
people = Person.objects.filter(name__isnull=True)

# получаем пользователей, у которых возраст установлен
people = Person.objects.filter(age__isnull=False)

regex и iregex
regex и iregex задают регулярное выражение, которому должно соответствовать значение свойства модели. В случае
с regex выборка зависит от регистра, а у iregex - не зависит от регистра.
# получаем пользователей, у которых имя заканчивается на am или om
people = Person.objects.filter(name__regex=r"(am|om)$")

спецификаторы дат
Целый ряд спецификаторов фильтрации предназначен для работы с датами:

date: значение поля должно соответствовать определенной дате. Представляет объект datetime.date

year: год даты должен соответствовать определенному значению.

month: определяет месяц даты

day: определяет день даты

week: определяет номер недели даты (1-52 или 53)

week_day: определяет день недели даты (от 1 (воскресенье) до 7 (суббота)

iso_week_day: определяет день недели даты (от 1 (понедельник) до 7 (воскресенье)

quarter: определяет номер квартала даты

time: определяет время даты. Представляет объект datetime.time

hour: определяет час даты (от 0 до 23)

minute: определяет минуту даты (от 0 до 59)

second: определяет секунду даты (от 0 до 59)

Все данные спецификаторы кроме date и time принимают целые числа. Допустим, у нас есть следующая модель:

from django.db import models

class Order(models.Model):
    datetime = models.DateTimeField()

from .models import Order
from datetime import datetime

# добавление начальных данных
if Order.objects.count() == 0:
    Order.objects.create(datetime = datetime(2021, 12, 26, 11, 25, 34))
    Order.objects.create(datetime = datetime(2022, 5, 12, 12, 25, 34))
    Order.objects.create(datetime = datetime(2022, 5, 22, 13, 25, 34))
    Order.objects.create(datetime = datetime(2022, 8, 19, 14, 25, 34))

# получаем заказы, сделанные в 5-м месяце
orders = Order.objects.filter(datetime__month=5)
for order in orders:
    print(order.datetime)


# получаем заказы, сделанные после 5-го месяца
orders = Order.objects.filter(datetime__month__gt=5)
for order in orders:
    print(order.datetime)

К спецификаторам дат можно добавлять дополнительные спецификаторы, чтобы конкретизировать условие, как во втором случае: datetime__month__gt=5

Поиск по дате и времени:

from .models import Order
from datetime import datetime, date, time

if Order.objects.count() == 0:
    Order.objects.create(datetime = datetime(2021, 12, 26, 11, 25, 34))
    Order.objects.create(datetime = datetime(2022, 5, 12, 12, 25, 34))
    Order.objects.create(datetime = datetime(2022, 5, 22, 13, 25, 34))
    Order.objects.create(datetime = datetime(2022, 8, 19, 14, 25, 34))

# получаем заказы, сделанные 22 мая
orders = Order.objects.filter(datetime__date=date(2022, 5, 22))
for order in orders:
    print(order.datetime)


# получаем заказы, сделанные после 12 часов
orders = Order.objects.filter(datetime__time__gt=time(12, 20, 0))
for order in orders:
    print(order.datetime)

Логические операторы
Логические операторы позволяют скомбинировать две выборки. Имеются следующие логические операторы: AND (&), OR (|) и XOR (^)

Оператор AND (&) указывает, что оба условия должны быть истинными:
people = Person.objects.filter(name="Tom") & Person.objects.filter(age=22)

В данном случае в базе данных будет идти поиск строки, в которой одновременно поле name равно "Tom" и поле age равно 22.
А на уровне базы данных это будет выражение:

SELECT ... WHERE name='Tom' AND age=22

Оператор OR (|) указывает, что достаточно, чтобы одно из двух условий было истинным:
people = Person.objects.filter(name="Tom") | Person.objects.filter(age=22)

В данном случае в базе данных будет идти поиск строки, в которой либо поле name равно "Tom", либо поле age равно 22.
А на уровне базы данных это будет выражение:
SELECT ... WHERE name='Tom' OR age=22

Оператор XOR (^) указывает, что необходимо, чтобы только одно из двух условий было истинно:
people = Person.objects.filter(name="Tom") ^ Person.objects.filter(age=22)

В данном случае в базе данных будет идти поиск строки, в которой истинно либо условие name="Tom", либо поле условие age=22,
но не одновременно оба условия. На уровне базы данных могут формироваться различные выражения в зависимости от поддержки оператора XOR.
"""