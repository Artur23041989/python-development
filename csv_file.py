import csv

"""
Функции обработки CSV-файлов

# csv.reader(csvfile, dialect='excel', **fmtparams) — возвращает объект reader, который построчно итерирует csvfile.
# Если csvfile является файловым объектом, то его нужно открыть с параметром newline=''.
# ополнительный параметр dialect используется для определения ряда параметров, характерных для специфического CSV диалекта.
# Он может быть подклассом Dialect или одной из строк, возвращаемой функцией list_dialects(). Также могут передаваться
# дополнительные ключевые аргументы fmtparams для переопределения отдельных параметров форматирования в текущем диалекте.
# Каждая строка, считанная из файла csv, возвращается в виде списка строк. Автоматическое преобразование типов данных
# не выполняется, если не указан параметр формата QUOTE_NONNUMERIC (в этом случае все поля без кавычек преобразуются
# в числа с плавающей точкой).

# Пример:
with open('eggs.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
     print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam


# csv.writer(csvfile, dialect='excel', **fmtparams) — возвращает объект writer, конвертирующий пользовательские
# данные в CSV-файл csvfile. csvfile может быть любым объектом с методом write(). Если csvfile является файловым
# объектом, то его нужно открыть с параметром newline=''. Параметры dialect и fmtparams идентичны параметрам в функции csv.reader.
# Необходимые методы экземпляра класса writer:
# csvwriter.writerow(row) — записывает данные, представляющие одну строку CSV в файл, форматируя согласно текущему диалекту writer.
# csvwriter.writerows(rows) — записывает данные, представляющие несколько строк CSV в файл, форматируя согласно текущему диалекту writer.

# Пример использования writer:
with open('eggs.csv', 'w', newline=' ') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                            qooting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])


# csv.field_size_limit([new_limit]) — текущий максимальный размер поля. Если задан new_limit, то он становится новым макс. размером.
# class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds) — как reader,
# но отображает информацию о столбцах в словарь, ключи которого заданы в параметре fieldnames.
# fieldnames это последовательность ключей. Если параметр опущен, в качестве ключей используются значения из первой
# строки файла. Если строка имеет больше полей, чем длина fieldnames, оставшиеся данные будут помещены в список с ключом
# из переменной restkey. Если строка имеет меньше полей, оставшиеся значения будут установлены в значение restval.
# Остальные аргументы пробрасываются далее в экземпляр reader.

# Пример использования:
with open('names.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
      print(row['first_name'], row['last_name'])
Eric Idle
John Cleese
print(row)
{'first_name': 'John', 'last_name': 'Cleese'}

# class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds) — как writer,
# но отображает словари в CSV-файл.
# Обязательный параметр fieldnames - последовательность ключей, определяющие порядок, в котором значения из словаря
# будут записаны в строке CSV-файла f.
# Параметр restval определяет значение в случае, если в словаре будет отсутствовать запись с данным ключом.
# Если словарь содержит лишние ключи, то поведение определяется параметром extrasaction. Если он 'raise', то выдаст ошибку.
# Если 'ignore', то такие ключи игнорируются.
# Остальные аргументы пробрасываются далее в экземпляр writer.
# Помимо методов writerow и writerows, DictWriter имеет также метод
# DictWriter.writeheader() — записывает данные строки заголовка в CSV-файл, форматируя согласно текущему диалекту writer.

# Пример использования DictWriter:
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# Диалекты и параметры форматирования
# class csv.Dialect — для упрощения задания формата входных и выходных записей, конкретные параметры форматирования
# группируются в диалекты, подклассы csv.Dialect. Диалекты поддерживают следующие атрибуты:

# Dialect.delimiter — разделитель столбцов в строке CSV-файла. По умолчанию ','.

# Dialect.quotechar — символ, использующийся для "склейки" поля, содержащего специальные символы, такие как delimiter,
# quotechar, или символы новой строки. По умолчанию используется значение '"'.

# Dialect.doublequote — как Dialect.quotechar, появляющийся внутри поля, должен экранироваться. Когда True, символ
# удваивается. Когда False, Dialect.escapechar используется как префикс к quotechar. По умолчанию True.
# При записи файла, если doublequote=False и не установлен escapechar, выдаст ошибку при обнаружении quotechar в столбце.

# Dialect.escapechar — символ, используемый writer для экранирования delimiter, если quoting установлен в QUOTE_NONE
# и quotechar, если doublequote=False. При чтении escapechar удаляет какое-либо особое значение со следующего символа.
# По умолчанию используется значение None, которое отключает экранирование.

# Dialect.lineterminator — символы, используемые для завершения строки при записи. По умолчанию '\r\n'.
# Dialect.skipinitialspace — если True, пробелы, непосредственно следующие за delimiter, игнорируются. Значение по умолчанию - False.
# Dialect.strict — когда True, поднимает исключение если CSV файл не распознается. По умолчанию - False.
# Dialect.quoting — контролирует, когда кавычки должны генерироваться writer и распознаваться reader.
# Он может принимать любые константы QUOTE_* и по умолчанию имеет значение QUOTE_MINIMAL.
# csv.QUOTE_ALL — writer оборачивает в кавычки все поля.
# csv.QUOTE_MINIMAL — writer оборачивает в кавычки только поля, содержащие специальные символы (delimiter, quotechar, lineterminator).
# csv.QUOTE_NONNUMERIC — writer оборачивает в кавычки все поля, не являющиеся числами. reader преобразует все поля без кавычек к типу float.
# csv.QUOTE_NONE — writer не оборачивает никакие поля в кавычки. Если в данных попадается
# delimiter или lineterminator, он предваряется символом escapechar, если установлен (исключение, если не установлен). reader не обрабатывает кавычки.
# csv.register_dialect(name[, dialect[, **fmtparams]]) — связывает dialect с именем name. Подробности о диалектах см. в разделе "Диалекты и параметры форматирования"
# csv.unregister_dialect(name) — удаляет связь диалекта с данным именем.
# csv.get_dialect(name) — возвращает класс диалекта, свзанного с именем name.
# csv.list_dialects() — список доступных диалектов. На данный момент это 'excel', 'excel-tab', 'unix'.

# Предустановленные диалекты

# class csv.excel — диалект CSV-файла, обычно генерируемого программой Excel.
# class csv.excel_tab — диалект CSV-файла, обычно генерируемого программой Excel с настройкой "разделитель с помощью TAB".
# class csv.unix_dialect — диалект CSV-файла, обычно генерируемого в UNIX-системах ('\n' для новой строки, закавычивание всех полей).

# Определение диалекта

# class csv.Sniffer — используется для угадывания диалекта CSV-файла. Имеет следующие методы:

# csvsniffer.sniff(sample, delimiters=None) — анализирует пример и возвращает Dialect, соответствующий обнаруженным
# параметрам. Если задан параметр delimiters, он интерпретируется как все возможные разделители.

# csvsniffer.has_header(sample) — анализирует текст и возвращает True, если первая строка похожа на строку заголовков.

# Методы определения диалекта являются эвристическими; это означает, что Sniffer может ошибаться.

# Пример использования Sniffer:

with open('example.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    # ... process CSV file contents here ...
    
# Примеры

# Простейший пример чтения CSV файла:

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Чтение файла формата passwd:

import csv
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

# Простейший пример записи CSV файла:

import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
"""