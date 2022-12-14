# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod

    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod

    def is_adult(age):
        return age > 18

person1 = Person('Maksym', 3)
person2 = Person.from_birth_year('Daniel', 2005)
print(person1.name, person1.age)
print(person2.name, person2.age)