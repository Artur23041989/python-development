text = ''' Я помню чудное мгновенье:
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

# 1. Количество символов в тексте
def count_total_characters(text):
    return len(text)

# 2. Количество букв в тексте
def count_letters(text):
    return sum(c.isalpha() for c in text)

# 3. Количество строк в тексте
def count_total_lines(text):
    return len(text.splitlines())

# 4. Количество непустых строк в тексте
def count_non_empty_lines(text):
    return sum(1 for line in text.splitlines() if line.strip())

# 5. Количество слов в тексте
def count_total_words(text):
    return sum(len(line.split()) for line in text.splitlines())

# 6. Анализ слов по строкам
def analyze_words_per_line(text):
    lines = text.splitlines()
    result = []
    for i, line in enumerate(lines, start=1):
        word_count = len(line.split())
        result.append(f"{i} строка - {word_count} слов")
    return result

# 7. Анализ символов по строкам
def analyze_characters_per_line(text):
    lines = text.splitlines()
    result = []
    for i, line in enumerate(lines, start=1):
        char_count = len(line)
        result.append(f"{i} строка - {char_count} символов")
    return result

# 8. Повторяющиеся слова
def find_repeated_words(text):
    words = [word.lower().strip('.,:;!?') for word in text.split()]
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return {word: count for word, count in word_count.items() if count > 1}

# 9. Частотный анализ текста
def frequency_analysis(text):
    letters = [char.lower() for char in text if char.isalpha()]
    frequency = {}
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency

# 10. Прочие символы
def count_other_characters(text):
    symbols = {}
    for char in text:
        if not char.isalnum() and not char.isspace():
            if char in symbols:
                symbols[char] += 1
            else:
                symbols[char] = 1
    return symbols

# Запись результатов в файл
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"1. Всего символов в тексте - {count_total_characters(text)}\n\n")
    f.write(f"2. Букв в тексте - {count_letters(text)}\n\n")
    f.write(f"3. Всего строк в тексте - {count_total_lines(text)}\n\n")
    f.write(f"4. Непустых строк в тексте - {count_non_empty_lines(text)}\n\n")
    f.write(f"5. Всего слов в тексте - {count_total_words(text)}\n\n")

    f.write("6. Анализ слов по строкам:\n")
    words_analysis = analyze_words_per_line(text)
    f.write("\n".join(words_analysis) + "\n\n")

    f.write("7. Анализ символов по строкам:\n")
    chars_analysis = analyze_characters_per_line(text)
    f.write("\n".join(chars_analysis) + "\n\n")

    repeated_words = find_repeated_words(text)
    f.write("8. Повторяющиеся слова:\n")
    for word, count in repeated_words.items():
        f.write(f"{word} - {count}\n")

    frequency = frequency_analysis(text)
    f.write("\n9. Частотный анализ текста:\n")
    for letter, count in frequency.items():
        f.write(f"{letter} - {count}\n")

    other_chars = count_other_characters(text)
    f.write("\n10. Прочие символы:\n")
    for char, count in other_chars.items():
        f.write(f"{char} - {count}\n")