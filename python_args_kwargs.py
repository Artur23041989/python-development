def get_info(name, age=34):
    print(name.title())
    print(age)

get_info(name='alex')


# * - распаковка списка
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)



# def print_scores(name, *scores): # * - в данном случае упаковка
#     print(f"name - {name}")
#     for i in scores:
#         print(i)
# print_scores('Dima', 26, 28, 32, 45, 68)




# def print_scores(name, first_test, *args):
#       print(f"name - {name}")
#       print(args[0])
#       print(args[1])
# print_scores('Dima', 26, 28, 32, 45, 68)
# def func(*args, **kwargs):
#     print(args)



# def func(name, lastname, *args, **kwargs):
#     print(args)
#     pass
# func(1, 2, 3, 4, 5)
# def func_2(a, b):
#     pass



# Вывод в столбик
# def print_pet_names(owner, **pets):
#     print(f'Владелец - {owner}')
#     for key, value in pets.items():
#         print(f"{key} - {value}")
#         или
#     for key in pets:
#         print(f'{key} - {pets[key]}')

# print_pet_names(owner='Dima', dog="Tima", cat="Barsic")



def print_pet_names(*args, **kwargs):
    print(f'Владелец - {args[0]}')
    for key in kwargs.keys():
        print(f"{key} - {kwargs[key]}")
print_pet_names('Alex', dog="Tusik", cat="Barsic")






