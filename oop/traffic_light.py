from time import sleep

class TrafficLight:  # создал класс светофор
    def __init__(self, color):
        self.color = color # словарь с цветами (ключами) и временем (значениями)

    def running(self):
        for key, value in self.color.items(): # цикл `for`, перебирает все пары "ключ-значение" в словаре
                                              # `self.color`. Метод `items()` возвращает итерацию по парам ключей
                                              # и значений словаря.
            sleep(value) # заставляет программу ждать указанное количество секунд
                         # (`value`) перед переходом к следующему цвету.
            print(key) # выводит текущий цвет


traffic_light = TrafficLight(color={ # создаю объект `traffic_light` класса `TrafficLight` с цветами и временами
                                     # их отображения: красный — 5 секунд, желтый — 2 секунды, зеленый — 5 секунд
    "Красный": 5,
    "Желтый": 2,
    "Зеленый": 5}
)
traffic_light.running() # вызываю метод "running" который показывает цвета