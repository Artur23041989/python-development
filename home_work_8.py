import string
from collections import Counter


text = '''
Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.

Шли годы. Бурь порыв мятежный
Рассеял прежние мечты,
И я забыл твой голос нежный,
Твои небесные черты.

В глуши, во мраке заточенья
Тянулись тихо дни мои
Без божества, без вдохновенья,
Без слез, без жизни, без любви.

Душе настало пробужденье:
И вот опять явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

И сердце бьется в упоенье,
И для него воскресли вновь
И божество, и вдохновенье,
И жизнь, и слезы, и любовь.
'''


def count_total_characters(text):
    return len(text)


def count_letters(text):
    return sum(c.isalpha() for c in text)


def count_total_lines(text):
    return len(text.splitlines())


def count_non_empty_lines(text):
    return sum(1 for line in text.splitlines() if line.strip())


def count_total_words(text):
    return len(text.split())


def count_words_per_line(text):
    return [len(line.split()) for line in text.splitlines()]


def count_characters_per_line(text):
    return [len(line) for line in text.splitlines()]


def find_repeated_words(text):
    words = text.split() # разделяю текст на [список] слов
    word_counts = Counter(words) # считаю количество повторяющихся слов {ключ - слово: значение - количество таких слов}
    return {word: count for word, count in word_counts.items() if count > 1} # возвращаем новый словарь, где кол-во
    # повторяющихся слов больше 1



def frequency_analysis(text):
    letters = [c for c in text if c.isalpha()]
    letter_counts = Counter(letters)
    total_letters = sum(letter_counts.values())
    return {letter: count / total_letters for letter, count in letter_counts.items()}


def find_non_alpha_characters(text):
    non_alpha = [c for c in text if not c.isalpha() and not c.isspace()]
    counter = Counter(non_alpha)
    return dict(counter)


# Записываем результаты в файл
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"1. Сколько всего символов в тексте: {count_total_characters(text)}\n")
    f.write(f"2. Сколько букв в тексте (без пробелов и знаков препинания): {count_letters(text)}\n")
    f.write(f"3. Сколько всего строк в тексте: {count_total_lines(text)}\n")
    f.write(f"4. Сколько непустых строк в тексте: {count_non_empty_lines(text)}\n")
    f.write(f"5. Сколько всего слов в тексте: {count_total_words(text)}\n")
    f.write(f"6. Сколько слов в каждой строке: {count_words_per_line(text)}\n")
    f.write(f"7. Сколько символов в каждой строке: {count_characters_per_line(text)}\n")
    f.write(f"8. Повторяющиеся слова в тексте: {find_repeated_words(text)}\n")
    f.write(f"9. Частотный анализ букв: {frequency_analysis(text)}\n")
    f.write(f"10. Посторонние символы (пробелы и знаки препинания): {find_non_alpha_characters(text)}\n")

