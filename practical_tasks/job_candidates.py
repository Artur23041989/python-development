"""
Имеется следующий список кандидатов на работу:
candidates = [
{'name': 'Дмитрий', 'age': 24, 'salary': 175000, 'skills': ['c#', 'c++', 'java']},
{'name': 'Алексей', 'age': 32, 'salary': 120000, 'skills': ['python', 'javascript', 'sql']},
{'name': 'Иван', 'age': 26, 'salary': 135000, 'skills': ['c#', 'c++', 'go']},
{'name': 'Екатерина', 'age': 35, 'salary': 78000, 'skills': ['c#', 'python', 'sql']},
{'name': 'Юлия', 'age': 42, 'salary': 80000, 'skills': ['python', 'sql']},
{'name': 'Мирон', 'age': 37, 'salary': 11000, 'skills': ['c#', 'c++', 'java']}
]
Задание:
1. Выведите на экран средний возраст кандидатов, округленный до целого числа
2. Выведите на экран среднюю желаемую зарплату, а также минимальную и максимальную
3. Выведите на экран имена кандидатов, знающих Python
4. Выведите на экран кандидатов, не знающих SQL
Пояснение: Для каждого из заданий напишите отдельную функцию
Пример вывода:
1. Средний возраст кандидатов - 25 лет
2. Средняя желаемая зарплата - 15300 рублей
3. Минимальная желаемая зарплата - 10000 рублей
4. Максимальная желаемая зарплата - 19000 рублей
5. Кандидаты, знающие Python: Максим, Валерий
6. Кандидаты, не знающие SQL: Елена, Артем
"""
candidates = [
{'name': 'Дмитрий', 'age': 24, 'salary': 175000, 'skills': ['c#', 'c++', 'java']},
{'name': 'Алексей', 'age': 32, 'salary': 120000, 'skills': ['python', 'javascript', 'sql']},
{'name': 'Иван', 'age': 26, 'salary': 135000, 'skills': ['c#', 'c++', 'go']},
{'name': 'Екатерина', 'age': 35, 'salary': 78000, 'skills': ['c#', 'python', 'sql']},
{'name': 'Юлия', 'age': 42, 'salary': 80000, 'skills': ['python', 'sql']},
{'name': 'Мирон', 'age': 37, 'salary': 11000, 'skills': ['c#', 'c++', 'java']}
]

def average_age(candidates): # создаю функцию, в которую в качестве аргумента передаю список кандидатов
    total_age = sum(candidate['age'] for candidate in candidates) # сумирую значения ключей ['age'] у каждого кандидата
                                                                  # и результат сохраняю в переменную 'total_age'
    avg_age = total_age / len(candidates) # здесь полученную сумму, которая находится в переменной 'total_age',
                                          # делю на общее количество кандидатов 'len(candidates)'
                                          # результат сохраняю в переменную 'avg_age'
    return round(avg_age) # возвращается средний возраст кандидатов с округлением возраста 'round'
avg_age = average_age(candidates) # результат функции 'average_age(candidates)' сохраняю в переменнуюa 'avg_age'
print(f"1. Средний возраст кандидатов - {avg_age} лет(года)")


def salary_statistic(candidates):
    salaries = [candidate['salary'] for candidate in candidates]
    avg_salary = sum(salaries) / len(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)
    return round(avg_salary), min(salaries), max(salaries)
"""
candidate['salary'] - это обращение к значению по ключу `'salary'` в каждом словаре 
`candidate`. Ожидается, что в каждом словаре, который представляет кандидата, есть 
ключ `'salary'`, значения которого мы и хотим извлечь.

for candidate in candidates - эта часть цикла проходит по каждому элементу (словарю) 
в списке `candidates`.

salaries = [...] - это создание нового списка, который будет содержать все значения зарплат, 
извлеченные из списка `candidates`
"""
avg_salary, min_salary, max_salary = salary_statistic(candidates)
print(f'2. Cредняя желаемая зарплата - {avg_salary} рублей')
print(f'3. Минимальная желаемая зарплата - {min_salary} рублей')
print(f'4. Максимальная желаемая зарплата - {max_salary} рублей')

def candidates_python(candidates):
    return [candidate['name'] for candidate in candidates
            if 'python' in candidate['skills']]
"""
`[candidate['name'] for candidate in candidates if 'python' in candidate['skills']]` — это синтаксис 
"генератора списков" (list comprehension). Он позволяет создавать новый список на основе существующего

`for candidate in candidates` - это цикл `for`, который перебирает каждого кандидата (`candidate`) в списке `candidates`

`if 'python' in candidate['skills']`: здесь идет условие, проверяющее, содержится ли строка `'python'` 
                                      в списке навыков (`skills`) текущего кандидата.

`candidate['name']`: если условие выполнено (т.е. у текущего кандидата есть навыки, содержащие 'python'), 
                     мы выбираем значение, связанное с ключом `'name'`, которое, как предполагается, хранит имя кандидата.
"""
python_candidates = candidates_python(candidates)
print(f'5. Кандидаты, знающие Python: {", ".join(python_candidates)}')

def candidates_sql(candidates):
    return [candidate['name'] for candidate in candidates
            if 'sql' not in candidate['skills']]
non_sql_candidates = candidates_sql(candidates)
print(f'6. Кандидаты, не знающие SQL: {", ".join(non_sql_candidates)}')










