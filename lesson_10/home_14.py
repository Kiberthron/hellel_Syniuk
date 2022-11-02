# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку.
# (результаты всех преобразований выводить на экран).

code = b'r\xc3\xa9sum\xc3\xa9'

result_1 = code.decode()
print(result_1)

result_2 = result_1.encode('latin1')
print(result_2)


result_3 = result_2.decode('latin1')
print(result_3)