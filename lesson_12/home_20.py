# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class auto:
    brand = 'audi'
    age = 5
    color = 'red'
    mark = 'a8'
    weight = 5000

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print(self.brand, self.mark, 'move')

    def birthday(self):
        self.age +=1
        print(self.age)

    def stop(self):
        print(self.brand, self.mark, 'stop')


a = auto('opel', 7, 'vectra')
a.move()
a.birthday()
a.stop()