
first = 1
result = 0
number = int(input("Ведите число: "))

for item in range(first, number+1):
    if item % 3 != 0:
        result += item ** 3

print(result)

result = 0
while number > 0:
    if number % 3 != 0:
        result += number ** 3
    number -= 1

print(result)
