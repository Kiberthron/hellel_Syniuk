# При помощи функции filter() из списка слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны),
# регистр букв не учитывать.
inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

import re


def check(text: str) -> bool:
    text = text.lower()
    if not text:
        return False

    return text == text[::-1]


data = list(filter(check, inputdata))
print(data)