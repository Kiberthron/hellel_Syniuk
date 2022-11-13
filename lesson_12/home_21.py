# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания. Класс 
# truck имеет дополнительный обязательный атрибут max_load. Переопределённый метод move, перед появлением надписи 
# «move» выводит надпись «attention», его реализацию сделать при помощи оператора super. А так же дополнительный 
# метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load» и снова пауза 1 сек. Класс car 
# имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи «move» должна
# появиться надпись «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума 
# max_speed. Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты. 

from time import sleep

class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print(self.brand, self.mark, 'move')


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load=2000):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()



    def load(selfself):
        sleep(1)
        print('load')
        sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed=300):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')



truck = Truck('SCANIA', 10, '"s 770"')
truck.load()
truck.move()


car = Car('VW', 3, 'Touran', 320)
car.move()