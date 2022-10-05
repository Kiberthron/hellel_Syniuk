board_id = "C02T41BPGTFM"
serial = "C02T41BPGTFM"
number = "C02T41BPGTFM"

print(board_id == serial == number)
print(id(board_id))
print(board_id is serial is number)


def main_function():
    global board_id
    global serial
    global number
    board_id = list(board_id)
    serial = list(serial)
    number = list(number)
    print(board_id == serial == number)
    print(id(board_id))
    print(id(serial))
    print(id(number))
    print(board_id is serial is number)


main_function()

print(type(board_id))
print(type(serial))
print(type(number))

model = [11]
model_id = [11]

print(id(model))
print(id(model_id))
print(model == model_id)
print(model is model_id)


def main_function():
    global model
    global model_id
    model = (" ".join(map(str, model)))
    model_id = (" ".join(map(str, model_id)))
    model = int(model)
    model_id = int(model_id)


main_function()

print(id(model))
print(id(model_id))
print(model == model_id)
print(model is model_id)
