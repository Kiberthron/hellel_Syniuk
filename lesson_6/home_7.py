# Сделать программу в виде функций в которой нужно будет угадывать число.
tries = 0
name = input("Введите имя: ")
print('Привет,', name, '. Угадай число от 1 до 10')


def play():
    import random
    global qnum, tries
    number = random.randint(1, 10)
    for tries in range(1, 5):
        qnum = input("Ваше число? ")
        if not qnum.isdigit() or int(qnum) <= 0:
            print("Ошибка, повторите ввод")
        elif int(qnum) < number:
            print('число слишком маленькое')
        elif int(qnum) > number:
            print('число слишком большое')
        elif int(qnum) == number:
            break
    if int(qnum) == number:
        tries = str(tries)
        print('Поздравляю,', name, 'Ты отгадал число с', tries, 'раза')
    elif int(qnum) != number:
        print('Увы,', name, ', не угадал')
    return qnum


play()
while True:
    answer = input("Желаете продолжить? (Д/Н) ")
    if answer.upper() in ("Y", "Д"):
        play()
    elif answer.upper() in ("N", "Н"):
        print('Спасибо , возращайся)')
        break
