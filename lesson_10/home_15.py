# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.


name = input('enter your name: ')
last_name = input('enter your last name: ')
birth = input('Your birthday: ')
age = input('age: ')

file = open('home_15.txt', 'w')
try:
    file.write(str(name) + '\n')
    file.write(str(last_name) + '\n')
finally:
    file.close()

file = open('home_15.txt', 'a')
try:
    file.write(str(birth) + '\n')
    file.write(str(age) + '\n')
finally:
    file.close()