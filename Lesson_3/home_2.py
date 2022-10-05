board_id = "C02T41BPGTFM"
serial = "C02T41BPGTFM"
number = "C02T41BPGTFM"

print(board_id == serial == number)
print(id(board_id))
print(board_id is serial is number)

def mainFunction():
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
mainFunction()

print(type(board_id))
print(type(serial))
print(type(number))

model = [11.1]
model_id = [11.1]

print(id(model))
print(id(model_id))
print(model == model_id)
print(model is model_id)

model_id = model

print(model == model_id)
print(model is model_id)













