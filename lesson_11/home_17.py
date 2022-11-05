chess_players = {286554: ("Carlsen", 34),
                 280445: ("Alireza", 23),
                 279954: ("Ding", 25),
                 279255: ("Magnus", 45),
                 277334: ("Fabiano", 40),
                 235555: ("Nepomniachtchi", 20)}


import json

with open('home_17.json',  'w') as f:
    json.dump(chess_players, f)

with open('home_17.json', 'r') as f:
    dt = json.load(f)
    indt = json.dumps(dt)
print(type(indt), indt)
