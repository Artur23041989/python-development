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
        self.is_power = False # указывает на то, что некое условие пока не выполнено

        # защищенный атрибут
        self._color = "green"

        # приватный атрибут
        self.__speed = 100

        # метод объекта
    def go(self):
        if self.is_power: # читается как если машина заведена (проверяем на True)
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
        if self.is_power: # проверяет, включено ли питание автомобиля. `self.is_power` предполагается как
                          # атрибут экземпляра класса, который хранит информацию о том, включен ли автомобиль.
            print("Car already is POWER ON")
        else:
            print(f"{self.brand} {self.model} POWER ON!")
            self.is_power = True # обновляет состояние автомобиля, устанавливая `is_power`
                                 # в значение `True`, что указывает на то, что автомобиль теперь включен.

    def power_off(self):
        if not self.is_power: # проверка на False, находится ли устройство в выключенном состоянии.
                              # Если `self.is_power` равно `False`, это значит, что устройство уже выключено
            print("Car already is POWER OFF")
        else: # если устройство включено, выполнится код внутри блока `else`.
            print(f"{self.brand} {self.model} POWER OFF!")
            self.is_power = False # состояние устройства обновляется: теперь `is_power` становится `False`,
                                  # что означает, что устройство выключено.

    def display_color(self):
        print(self._color)

    def set_color(self, new_color):
        if new_color in Car._COLORS: # если new_color входит в _COLORS то
            self._color = new_color
        else:  # иначе
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
        self.__speed = 200

    def tilt_trailer(self):
        print(f'{self.brand} {self.model} tilt trailer')

    def display_speed(self):
        print(self.__speed)

    def power_off(self):
        super().power_off()
        print('The method of Truck class')


car_audi = Car(brand='Audi', model='A6', year=2022, power=249)
car_bmw = Car(brand='BMW', model='X5', year=2022, power=333)

truck = Truck(brand='Volvo', model='xxx', year=2019, capasity=4000, axles=6, power=700)
truck.power_on()
truck.tilt_trailer()
truck.power_off()
truck.display_color()
print(truck.speed)
truck.display_speed()
print(dir(truck))




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


