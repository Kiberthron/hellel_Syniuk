# Создать свой класс String на базе стандартного класса str.
# В нём необходимо:
#     • переопределить стандартный метод отвечающий за сложение
#     • написать отсутствующий в классе str метод отвечающий за вычитание
#
# Принцип работы сложения в новом классе String: объект типа String можно
# складывать как друг с другом, так и с любым другим типом, который может
# быть приведён к строковому типу. "Под капотом" оба операнда приводятся к
# строковому типу и происходит конкатенация двух строк. Примеры выполнения:
# String('New') + String(890)    ->    'New890'
# String(1234) + 5678    ->    '12345678'
# String('New') + 'castle'    ->    'Newcastle'
# String('New') + 77    ->    'New77'
# String('New') + True    ->    'NewTrue'
# String('New') + ['s', ' ', 23]    ->    "New['s', ' ', 23]"
# String('New') + None    ->    'NewNone'
#
# Принцип работы вычитания в новом классе String: из объекта типа String
# можно вычесть значение любого другого типа, которое может быть приведёно к
# строковому типу. "Под капотом" оба операнда приводятся к строковому типу и
# затем из первого операнда убирается первое вхождение второго операнда,
# если таковое имеется. Если в первом операнде не находится значение второго
# операнда, то результатом вычитания будет первый операнд без изменений.
# Примеры выполнения:
# String('New bala7nce') - 7    ->    'New balance'
# String('New balance') - 'bal'    ->    'New ance'
# String('New balance') - 'Bal'    ->    'New balance'
# String('pineapple apple pine') - 'apple'    ->    'pine apple pine'
# String('New balance') - 'apple'    ->    'New balance'
# String('NoneType') - None    ->    'Type'
# String(55678345672) - 7    ->    '5568345672'
#
# *Важно! Результатом сложения или вычитания всегда будет объект типа String.


class String():
    def __init__(self, string1, string2):
        self.string1 = str(string1)
        self.string2 = str(string2)
        self.string1_string2 = str(string1) + str(string2)

c = String('new', 890)
print(type(c.string1_string2), c.string1_string2)
c = String('New', ['s', ' ', 23])
print(type(c.string1_string2), c.string1_string2)

print('-' *50)

class String():
    def __init__(self, string1, string2):
        self.string1 = str(string1)
        self.string2 = str(string2)
        self.string1_string2 = self.string1.replace(self.string2, '')

c = String('New bala7nce', '7')
print(type(c.string1_string2), c.string1_string2)
c = String('New balance', 'bal')
print(type(c.string1_string2), c.string1_string2)

