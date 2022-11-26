# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def degree (x, y):
    return x ** y


operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '**': degree
}

while True:
    sign = input('Знак (+, -, *, /, **): ')
    if sign == 'exit':
        break
    try:
        operation = operations[sign]
        x = float(input('x = '))
        y = float(input('y = '))
        print('{0:.2f}'.format(operation(x, y)))
    except KeyError:
        print('Неверный знак операции!')
    except ZeroDivisionError:
        print('Деление на 0!')
    except ValueError:
        print('Не удалось преобразовать в число!')

