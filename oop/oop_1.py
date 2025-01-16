"""
ООП - объектно-ориентированное программирование
Класс - общее описание предметной области на языке программирования
Объект - экземпляр (конкретный представитель класса)
Метод - функция, связанная с объектом класса (классом)
Атрибут - характеристика (свойства) объекта или класса
Конструктор - метод, который управляет созданием объекта

Инкапсуляция - механизм, позволяющий скрывать внутренние детали реализации объекта
и предоставлять доступ к ним только через определенные методы, чтобы защитить
данные и контролировать доступ к ним
"""
class Car:
    _COLORS = ("red", "green", "blue", "")

    def __init__(self, brand, model, year, power, currrence="RUB"):
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.country = "Armenia"
        self.currence = currrence
        self.is_power = False

        # защищенный атрибут
        self._color = ""

        # приватный атрибут
        self.__speed = 100

        # метод объекта
    def go(self):
        if self.is_power:
           print(f"{self.brand} {self.model} TO GO!")
        else:
            print("Car must be POWER ON")

    def stop(self):
        if self.is_power:
            print(f"{self.brand} {self.model} STOP!")
        else:
            print("Car must be POWER ON")

    def turn(self, direction):
        if self.is_power:
            print(f"{self.brand} {self.model} TURN {direction.upper()}")
        else:
            print("Car must be POWER ON")

    def power_on(self):
        if self.is_power:
            print("Car already is POWER ON")
        else:
            print(f"{self.brand} {self.model} POWER ON!")
            self.is_power = True

    def power_off(self):
        if not self.is_power:
            print("Car already is POWER OFF")
        else:
            print(f"{self.brand} {self.model} POWER OFF!")
            self.is_power = False

    def display_color(self):
        print(self._color)

    def set_color(self, new_color):
        if new_color in Car._COLORS:
            self._color = new_color
        else:
            raise ValueError("Неправильный цвет")

    # Getter для получения значения скорости
    @property
    def speed(self):
        return self.__speed

    # Setter для получения значения скорости
    @speed.setter
    def speed(self, value):
        if value > 300:
            raise ValueError('Max speed 300')
        self.__speed = value


# Дочерний класс грузовых машин
class Truck(Car):
    # указываем характеристики родительского и новые характеристики дочернего класса
    def __init__(self, brand, model, year, power, capasity, axles, currrence="RUB"):
        # вызываем конструктор родительского класса с его параметрами через функцию super()
        super().__init__(brand, model, year, power, currrence="RUB")
        self.capasity = capasity
        self.axles = axles

    def tilt_trailer(self):
        print(f'{self.brand} {self.model} tilt trailer')

    def power_off(self):
        super().power_off()
        print('The method of Truck class')


car_audi = Car(brand='Audi', model='A6', year=2022, power=249)
car_bmw = Car(brand='BMW', model='X5', year=2022, power=333)

truck = Truck(brand='Volvo', model='xxx', year=2019, capasity=4000, axles=6, power=700)
truck.power_on()
truck.tilt_trailer()
truck.power_off()



# print(car_bmw.speed)

# car_bmw.speed = 400





# car_audi.power_off()
# car_audi.go()
# car_audi.turn(direction="left")
#
#
# car_audi.power_on()
# car_audi.power_on()
# car_audi.go()
# car_audi.turn(direction="left")
# car_audi.power_off()
#
# # car_audi.set_color(new_color="black")
# # car_audi.display_color()
#
# print(dir(car_audi))
# print(car_audi._Car__speed)


