while True:
    name = input("Введите имя: ")
    age = input("Сколько Вам лет: ")
    if not age.isdigit() or int(age) <= 0:
        print("Ошибка, повторите ввод")
    elif int(age) < 10:
        print("Привет, шкет", name)
    elif int(age) <= 18:
        print("Как жизнь", name)
    elif int(age) < 100:
        print("Что желаете", name)
    else:
        print(name, "вы лжете - в наше время столько не живут", sep=', ')
    answer = input("Желаете выйти? (Д/Y) ")
    if answer.upper() in ("Y", "Д"):
        break
