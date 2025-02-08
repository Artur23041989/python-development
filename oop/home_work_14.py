class Animal:
    def __init__(self, name, view, height, weight):
        self.name = name
        self.view = view
        self.height = height
        self.weight = weight
        self._color = " "
        self.__age = 5

    def walk(self):
        print(f'{self.name} гуляет!')

    def eat(self):
        print(f'{self.name} кушает.')

    def sit(self):
        print(f'{self.name} сидит.')

    def sleep(self):
        print(f'{self.name} лег спать!')

    def _sound(self):
        print(f'{self.name} издает звуки!')

    def __privat(self):
        print("Приватный метод")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

class Cat(Animal):
    def __init__(self, name, view, height, weight, breed, energy, noisiness):
        super().__init__(name, view, height, weight)
        self.breed = breed
        self.energy = energy
        self.noisiness  =noisiness

    def purr(self):
        print(f'{self.name} мурлыкает!')

    def climb(self):
        print(f'{self.name} залез на шкаф.')

    def scratch(self):
        print(f'{self.name} поцарапал диван!')

    def walk(self):
        super().walk()
        print('The method of Animal class')


# animal = Animal(name='Archi', view='dog', height=50, weight=4)
# animal.walk()
# animal.eat()
# animal.sit()
# animal.sleep()
# animal.age = 2
# animal._color = 'black'
# print(animal._color)
# animal._sound()
# print(animal.age)


cat = Cat(name='Barsic', view='xxx', height=45, weight=2, breed='Pers', energy=100, noisiness='тихий')
cat.purr()
cat.climb()
cat.scratch()
cat.walk()















