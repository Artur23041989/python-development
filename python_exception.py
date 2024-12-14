import requests

"""
try:
    блок,
    где возможна
    ошибка
except:
    действия,
    в случае
    ошибки
finally: применяется редко!!!
    блок кода,
    который выполнится в любом случае
"""
from http.client import responses

from urllib3 import request


# age = input('Enter the age: ')
# try:
#     if age < 18:
#         print('error')
#     else:
#         print('ok')
# except:
#     print('Возникла ошибка')


# age = input('Enter the age: ')
# try:
#     if age < 18:
#         print('error')
#     else:
#         print('ok')
# except:
#     if age.isdigit():
#         if int(age) < 18:
#             print('error')
#         else:
#             print('ok')
#     else:
#         print('не число')



# def send_data():
#     data = {'name': 'Alex', 'age': 26}
#     data = None
#     return Exception('ERROR')
#
# def get_data_from_server():
#     try:
#         data = send_data()
#         print(data)
#     except:
#         data = []
#         for i in data:
#             print(i)
# get_data_from_server()



# try:
#     mydict = {'name': 'dima'}
#     if not mydict.get('age'):
#         print(mydict.get('age'))
#         raise Exception('Такого ключа нет!!!')
# except Exception as err: обработать как переменную err
#     print(err)



# def check_age(age):
#     if age > 102:
#         raise  Exception('Возраст слишком большой')
#     return  age
## try:
#     print(check_age(226))
# except:
#     print('Возникла ошибка')




# HTTP
# def get_page(url):
#     response = requests.get(url)
#     print(response.status_code)
#     print(response.text)
#
# url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
# get_page(url)



# Имитируем ошибу 'ruuu'
# def get_page(url):
#     try:
#         response = requests.get(url) - отправка запроса, в переменную занесится ответ от сервера
#         print(response.status_code)
#         print(response.text)
#     except:
#         print("Error")
#     print('code')
# url = "https://ruuu.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
# get_page(url)


"""
Пишем функцию, которая будет проходить по всем 
символам в строке и суммировать те, которые являются цыфрами
"""
number_str = '1a2a3a4a5'
def get_sum_numbers(number_str):
    a = 0
    for char in number_str:
        if char.isdigit():
            a +=int(char)
    return a
result = get_sum_numbers(number_str)
print(result)











