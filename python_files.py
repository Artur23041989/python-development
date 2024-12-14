import os
import shutil
from fileinput import filename
from python_dict import users_info


# функция open(file, mode, encoding) - открывает файл
# file - путь к файлу (абсолютный или относительно скрипта)
# mode - режим открытия файла
# encoding - кодировка

# Основные режимы: r - чтение, w - запись с пересозданием файла, a - добавление в конец файла




myfile = open(file='myfile.txt', mode='w', encoding='utf-8')
# write - запись в файл
myfile.write('Python!!!\n')
text = 'Forever!!!\n'
myfile.write(text)

# my_list = ['alena', 'elena']
# for item in my_list:
#     myfile.write(item+'\n')


# my_list = ['alena', 'elena']
# names = '\n'.join(my_list)
# myfile.write(names)


my_list = ['alena', 'elena!']
for item in my_list:
    myfile.write(item.strip(',!')+'\n')


# после завершения работы с файлом закрываем его
myfile.close()


# открытие файла в режиме (а) добавления в конец файла
myfile = open(file='myfile.txt', mode='a', encoding='utf-8')
myfile.write('Python!!!\n')
# myfile.writelines(my_list) - добавляет и склеевает текст
myfile.close()


# открытие файла для чтения
myfile = open(file='myfile.txt', mode='r', encoding='utf-8')
text_from_file = myfile.read()
text_rows = text_from_file.split('\n')
print(text_rows)

#myfile.seek(0)
#text_lines = myfile.readlines()
#print(text_lines[0], text_lines[1])
# print(text_lines)


mylist = ['alex', 'ivanov']
print(*mylist, sep='\n')


# with open(file='myfile.txt', mode='r', encoding='utf-8') as my_file:  # с функцией открытия файла связать my_file
#     text_form_f = my_file.read()
# print(text_form_f)


file_name = 'myfilenew.txt'
# проверка существования пути к файлу
if os.path.exists(file_name):
    with open(file=file_name, mode='r', encoding='utf-8') as my_file:
        text_form_f = my_file.read()
else:
    with open(file=file_name, mode='w', encoding='utf-8') as my_file:
        pass


# rename file
# if os.path.exists(file_name):
#     file_name_new = f"new_{file_name}"
#     os.rename(file_name, file_name_new)

# if os.path.exists(file_name):
#     os.remove(file_name_new)


filename_new = f"new_{file_name}"
if os.path.exists(file_name):
    os.rename(file_name, filename_new)
    print(f'Файл {file_name} --> {filename_new}')


if os.path.exists(filename_new):
    os.remove(filename_new)
    print(f'Файл {filename_new} удален!')


# создаем каталог
dir_name = 'files'
if not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=True)

os.makedirs(dir_name, exist_ok=True)


# удаление каталога
#os.rmdir(dir_name)
with open(file=f'{dir_name}/{file_name}', mode='w', encoding='utf-8') as my_file:
    pass

shutil.rmtree(dir_name)


info = {
    'name': 'Alex',
    'age': 24,
    'lang': ['python', 'js'],
    'phones': {
        'first_mob': '233543664',
        'second_mob': '4546478',
    }
},
{
    'name': 'Alex',
    'age': 24,
    'lang': ['python', 'js'],
    'phones': {
        'first_mob': '233543664',
        'second_mob': '4546478',
    }
}
]

with open('user.json', 'w') as file:
    json.dump(users_info, file)








