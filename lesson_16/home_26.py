# Создать генератор геометрической прог



def geom_generator(max_number):
  i = 1
  while i < max_number:
    yield i
    i = i*2

for i in geom_generator(max_number=1000):
  print (i)