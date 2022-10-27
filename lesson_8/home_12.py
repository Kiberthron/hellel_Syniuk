# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()
from datetime import datetime


def decorator(result):
    time = datetime.now()
    print("Used time:", datetime.now() - time)
    return result


@decorator
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


list_num = [1, 1, 3, 2, 1, 3, 4, 6, 4, 1, 4, 6, 3, 2, 6, 8, 9, 8]
dic1 = {}

analysis(list_num, dic1)

for item in dic1:
    print("'%d':%d" % (item, dic1[item]))


@decorator
def check(text: str) -> bool:
    text = text.lower()
    if not text:
        return False

    return text == text[::-1]


inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

data = list(filter(check, inputdata))
print(data)
