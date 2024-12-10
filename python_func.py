def hello():
    print('Hello')
hello()




def bye():
        print('Bye')
bye()




def print_name(name):
    print(name)
# name = "Masha"
# last_name = "Dima"
# print_name(name = "Maxim")
# print_name(name = name)
# print_name(name = last_name)



# сигнатура функции - имя и параметры
def print_info(name, lastname, age, city='SPb'):
    info = {
        'name': name,
        'lastname': lastname,
        'age': age,
        'city': city
    }
    print(info)
    return info
user_name = "Dmitry"
user_lastname = 'Ivanov'
user_age = 32
user_city = 'Moscow'
# именованные аргументы
#print_info(name=user_name,age=user_age, city=user_city, lastname=user_lastname)

# позиционные аргументы
# print_info(user_city, user_name, user_lastname, user_age)

# комбинированный способ (именованные аргументы должны следовать за позиционными!!!)
# print_info(city=users_city, user_name, user_age, user_lastname)

result = print_info(name=user_name, age=user_age, lastname=user_lastname, city='Moscow')
print(result)




def text_analyse(text):
    stat = {}
    for s in text:
        stat[s] = text.count(s)
    return stat

print(text_analyse(text='hello'))



def text_to_list(text: str):
    return text.split(' ')
print(text_to_list(text="I love python string"))



def text_to_list(text: str)-> list[int]:
    return text.split(' ')
print(text_to_list(text="I love python string"))

emails = [
    "admin@mail.ru",
    "alexey@mail.ru",
    "sasha@yandex.ru",
    "igor@gmail.ru"
]
def get_emails(in_emails: list[str], domen: str = '.ru') -> list:
    emails = []
    for email in in_emails:
        if email.endswith(domen):
            emails.append(email)

    return emails

print(get_emails(in_emails=emails))


def check_age(age: int|str)-> bool:
    if isinstance(age, int):
        if age < 18:
            return  False
        else:
             return  True
    if isinstance(age, str):
        if age.isdigit():
            if int(age) < 18:
                return False
            else:
                return True
        else:
            return False

age = '12'
if check_age(age):
    print('OK')
else:
    print('ERROR!!!')



