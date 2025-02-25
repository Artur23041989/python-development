import random
import string

class PasswordGenerator: # по умолчанию в пароле используются маленькине буквы и цифры
    special_chars = "!#?%&()_*@" # могут использоваться в пароле, когда включена соответствующая опция

    def __init__(self,
                 min_length=6, # минимальная длина пароля
                 max_length=12, # максимальная длина пароля
                 use_uppercase=False, # по умолчанию заглавные буквы выключены
                 use_special_chars=False): # по умолчанию специальные символы выключены
        self.min_length = min_length
        self.max_length = max_length
        self.use_uppercase = use_uppercase
        self.use_special_chars = use_special_chars

    def generate_password(self):
        if self.min_length > self.max_length:
            raise ValueError("Минимальная длина не может быть больше максимальной")
        length = random.randint(self.min_length, self.max_length) # создаем переменную, в которую будет
                                                                  # сохранено случайное число длиной от 6 до 12

        characters = string.ascii_lowercase + string.digits # эта запись дает нам все буквы в нижнем регистре плюс цифры
        if self.use_uppercase: # если опция включена то прибавятся символы с большой буквы
            characters += string.ascii_uppercase

        if self.use_special_chars: # если опция включена то прибавятся специальные символы
            characters += PasswordGenerator.special_chars

        password = "".join(random.choice(characters) for _ in range(length))
        """
        "".join() — эта конструкция объединяет все выбранные символы в одну строку.
                    Метод `join` берёт последовательность строк и объединяет их в одну строку,
                    используя способ объединения, указанный перед вызовом метода. Поскольку перед ним
                    стоит пустая строка `""`, символы будут соединены без каких-либо разделителей.
        random.choice(characters) — эта функция выбирает один случайный элемент из последовательности `characters`.
                                    Предполагается, что `characters` — это строка или какой-то другой список символов
                                    (например, буквы, цифры, специальные знаки), из которых будет составлен пароль.
        for _ in range(length) — это цикл, который выполняется `length` раз. 
                                `length` — это переменная, которая задает длину пароля
        """
        return password

password_generator = PasswordGenerator(use_uppercase=True, use_special_chars=True)
print(password_generator.generate_password())

