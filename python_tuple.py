# кортеж - неизменяемый список
# создание кортежа

colors_1 = tuple()
colors_2 = ('red', 'green')
print(id(colors_2))
colors_2 = colors_2 + ('yellow',)
print(id(colors_2))
print(colors_2)

colors = (
    ('red', 'красный'),
    ('green', 'зеленый'),
    ('blue', 'синий')
)